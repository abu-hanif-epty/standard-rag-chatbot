from app.ingestion.loader import load_documents
from app.ingestion.chunking import split_documents
from app.retrieval.vector_store import create_vector_store


def main():

    print("Loading documents...")

    documents = load_documents()

    print(f"Loaded documents: {len(documents)}")

    print("Splitting documents...")

    chunks = split_documents(documents)

    print(f"Total chunks: {len(chunks)}")

    print("Creating vector database...")

    vector_store = create_vector_store(chunks)

    print("Indexing completed successfully!")
    print("Stored chunks:", vector_store._collection.count())


if __name__ == "__main__":
    main()