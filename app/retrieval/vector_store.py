
from langchain_chroma import Chroma

from app.config import CHROMA_DB_DIR, COLLECTION_NAME
from app.retrieval.embeddings import get_embeddings


def get_vector_store():
    embeddings = get_embeddings()

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_DB_DIR
    )

    return vector_store


def add_documents_to_store(chunks, chunk_ids):
    vector_store = get_vector_store()

    if chunks:
        vector_store.add_documents(
            documents=chunks,
            ids=chunk_ids
        )

    return vector_store


def load_vector_store():
    return get_vector_store()
