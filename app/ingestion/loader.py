from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from app.config import DOCUMENTS_DIR


def load_documents():
    documents = []

    for file_path in Path(DOCUMENTS_DIR).iterdir():

        if file_path.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(file_path))
            
        elif file_path.suffix.lower() == ".txt":
            loader = TextLoader(str(file_path), encoding="utf-8")
        else:
            continue

        loaded_docs = loader.load()
        documents.extend(loaded_docs)

    return documents