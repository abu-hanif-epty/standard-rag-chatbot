from langchain_chroma import Chroma

from app.config import CHROMA_DB_DIR, COLLECTION_NAME
from app.retrieval.embeddings import get_embeddings


def create_vector_store(chunks):

    embeddings = get_embeddings()

    # Connect to existing collection
    existing_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_DB_DIR
    )

    # Remove old records
    existing_store.delete_collection()

    # Create a fresh database
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR,
        collection_name=COLLECTION_NAME
    )

    return vector_store


def load_vector_store():

    embeddings = get_embeddings()

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_DB_DIR
    )

    return vector_store