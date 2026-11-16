from app.retrieval.vector_store import load_vector_store
from app.config import TOP_K


def get_retriever():

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K}
    )

    return retriever