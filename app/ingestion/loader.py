
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader, TextLoader


def load_single_document(file_path):
    file_path = Path(file_path)

    if file_path.suffix.lower() == ".pdf":
        loader = PyPDFLoader(str(file_path))

    elif file_path.suffix.lower() == ".txt":
        loader = TextLoader(str(file_path), encoding="utf-8")

    else:
        return []

    return loader.load()
