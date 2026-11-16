
import hashlib
import json
from pathlib import Path

from app.config import DOCUMENTS_DIR, MANIFEST_PATH
from app.ingestion.loader import load_single_document
from app.ingestion.chunking import split_documents
from app.retrieval.vector_store import (
    get_vector_store,
    add_documents_to_store
)


def calculate_file_hash(file_path):
    """Generate SHA-256 hash for a document."""

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for block in iter(lambda: file.read(4096), b""):
            sha256.update(block)

    return sha256.hexdigest()


def load_manifest():
    """Load previously indexed document information."""

    if not Path(MANIFEST_PATH).exists():
        return {}

    with open(MANIFEST_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def save_manifest(manifest):
    """Save manifest safely."""

    temp_path = MANIFEST_PATH + ".tmp"

    with open(temp_path, "w", encoding="utf-8") as file:
        json.dump(manifest, file, indent=4)

    Path(temp_path).replace(MANIFEST_PATH)


def get_existing_sources(vector_store):
    """Get source filenames already stored in ChromaDB."""

    result = vector_store._collection.get(
        include=["metadatas"]
    )

    sources = set()

    for metadata in result.get("metadatas", []):
        if metadata and metadata.get("source"):
            sources.add(Path(metadata["source"]).name)

    return sources


def main():

    print("=" * 45)
    print("       INCREMENTAL DOCUMENT INGESTION")
    print("=" * 45)

    manifest = load_manifest()

    vector_store = get_vector_store()

    # Detect documents indexed before we introduced the manifest.
    existing_sources = get_existing_sources(vector_store)

    document_files = [
        file for file in Path(DOCUMENTS_DIR).iterdir()
        if file.suffix.lower() in [".pdf", ".txt"]
    ]

    if not document_files:
        print("No PDF or TXT documents found.")
        return

    added_count = 0
    skipped_count = 0

    for file_path in document_files:

        print(f"\nChecking: {file_path.name}")

        file_hash = calculate_file_hash(file_path)

        # Already indexed by content hash.
        if file_hash in manifest:
            print("Already indexed. Skipping.")
            skipped_count += 1
            continue

        # Recognize files already in the old database.
        if file_path.name in existing_sources:
            print("Already exists in database. Skipping embedding.")

            manifest[file_hash] = {
                "filename": file_path.name,
                "source": str(file_path)
            }

            save_manifest(manifest)
            skipped_count += 1
            continue

        try:
            # 1. Load one document.
            print("Loading document...")
            documents = load_single_document(file_path)

            if not documents:
                print("No readable content. Skipping.")
                continue

            # 2. Add tracking metadata.
            for document in documents:
                document.metadata["source_hash"] = file_hash

            # 3. Split into chunks.
            print("Splitting document...")
            chunks = split_documents(documents)

            if not chunks:
                print("No chunks generated. Skipping.")
                continue

            # 4. Generate stable IDs for chunks.
            chunk_ids = [
                hashlib.sha256(
                    f"{file_hash}_{index}".encode("utf-8")
                ).hexdigest()
                for index in range(len(chunks))
            ]

            # 5. Add new chunks to existing database.
            print("Embedding and storing new document...")
            add_documents_to_store(chunks, chunk_ids)

            # 6. Update manifest only after successful indexing.
            manifest[file_hash] = {
                "filename": file_path.name,
                "source": str(file_path),
                "chunks": len(chunks)
            }

            save_manifest(manifest)

            print(f"Successfully indexed: {file_path.name}")
            print(f"Chunks added: {len(chunks)}")

            added_count += 1

        except Exception as error:
            print(f"Failed to index {file_path.name}: {error}")

    print("\n" + "=" * 45)
    print("INGESTION SUMMARY")
    print("=" * 45)
    print(f"New documents added: {added_count}")
    print(f"Documents skipped: {skipped_count}")
    print(f"Total chunks in database: {vector_store._collection.count()}")


if __name__ == "__main__":
    main()
