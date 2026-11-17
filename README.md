# Improved RAG Chatbot

An improved version of the Standard RAG Chatbot with incremental document ingestion.

The main objective is to add new documents to the existing vector database without deleting or replacing previously stored embeddings.

## New Features

- Supports PDF and TXT documents
- Incremental document ingestion
- Add new documents without deleting previous embeddings
- Preserve existing vector database records
- Avoid duplicate document ingestion using document tracking
- Document manifest management
- Improved document management workflow

## Key Improvement: Incremental Ingestion

In the original version, document ingestion is performed as a basic ingestion process.

In this improved version, the ingestion system checks which documents are new and processes only those documents.

### How It Works

1. Add a new PDF or TXT file to the documents folder.
2. Run the ingestion script.
3. The system checks the document manifest.
4. New documents are extracted and chunked.
5. Embeddings are generated only for new documents.
6. New embeddings are added to the existing ChromaDB database.
7. Previously stored embeddings remain unchanged.

## Incremental Ingestion Workflow

```text
New PDF/TXT Document
        |
        v
Document Detection
        |
        v
Check Document Manifest
        |
        v
Is Document New?
        |
        v
Text Extraction
        |
        v
Text Chunking
        |
        v
Generate Embeddings
        |
        v
Add to Existing ChromaDB
        |
        v
Update Document Manifest
```

## Technologies Used

- Python
- LangChain
- ChromaDB
- Embedding Models
- Groq API
- LLM
- JSON (Document Manifest)

## Installation

Clone the repository:

```bash
git clone https://github.com/abu-hanif-epty/standard-rag-chatbot.git
cd standard-rag-chatbot
```

Switch to the improved branch:

```bash
git checkout improve
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
```

## Run the Project

Add your PDF or TXT documents to the document folder.

Run:

```bash
python ingestion.py
```

Start the chatbot:

```bash
python main.py
```

## Main Advantage

Unlike the basic ingestion approach, this version preserves previously stored embeddings and adds only newly detected documents.

This makes document management more efficient and prevents unnecessary reprocessing.

## Project Goal

To develop a more practical and maintainable RAG system with incremental document ingestion and persistent vector database storage.
