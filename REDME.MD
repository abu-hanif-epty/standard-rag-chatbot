# Standard RAG Chatbot

A terminal-based Retrieval-Augmented Generation (RAG) chatbot that answers questions using information from your own documents.

## Features

- PDF and TXT document support
- Document text extraction
- Recursive text chunking
- Text embedding generation
- Vector database storage using ChromaDB
- Semantic similarity search
- Context-based answer generation using an LLM
- Source-based responses

## How It Works

1. Load PDF and TXT documents.
2. Extract text from documents.
3. Split text into smaller chunks.
4. Generate embeddings for each chunk.
5. Store embeddings in ChromaDB.
6. Retrieve relevant chunks based on user questions.
7. Send retrieved context to the LLM.
8. Generate an answer based on the provided documents.

## Project Workflow

```text
Documents (PDF/TXT)
        |
        v
   Text Extraction
        |
        v
   Text Chunking
        |
        v
   Embeddings
        |
        v
     ChromaDB
        |
        v
   User Question
        |
        v
    Retrieval
        |
        v
   LLM Response
```

## Technologies Used

- Python
- LangChain
- ChromaDB
- Embedding Models
- Groq API
- LLM

## Installation

Clone the repository:

```bash
git clone https://github.com/abu-hanif-epty/standard-rag-chatbot.git
cd standard-rag-chatbot
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
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

Run the ingestion script first:

```bash
python ingestion.py
```

Then start the chatbot:

```bash
python main.py
```

## Project Goal

The goal of this project is to understand and implement the fundamental concepts of Retrieval-Augmented Generation, including document processing, embeddings, vector databases, retrieval, and LLM-based response generation.
