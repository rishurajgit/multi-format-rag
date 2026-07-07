# Multi-Format RAG Assistant

A Retrieval-Augmented Generation (RAG) application built with **FastAPI**, **LangChain**, **Google Gemini**, and **ChromaDB**. The application allows users to upload PDF documents, generate embeddings, store them in a vector database, and ask natural language questions based on the uploaded content.

---

## Features

- Upload PDF documents
- Validate uploaded files
- Extract text using PyPDFLoader
- Split documents into chunks using RecursiveCharacterTextSplitter
- Generate embeddings using Google Gemini
- Store document embeddings in ChromaDB
- Retrieve relevant document chunks using semantic search
- Generate context-aware answers using Gemini LLM
- Return source citations including:
  - Document Name
  - Page Number
  - Chunk ID
- Interactive API documentation using FastAPI Swagger

---

## Tech Stack

- Python 3.13
- FastAPI
- LangChain
- Google Gemini API
- ChromaDB
- Pydantic Settings
- UV Package Manager

---

## Project Structure

```text
multi-format-rag/
│
├── app/
│   ├── core/
│   │   └── prompt.py
│   │
│   ├── db/
│   │   └── chroma_db.py
│   │
│   ├── loaders/
│   │   └── document_loader.py
│   │
│   ├── processing/
│   │   └── splitter.py
│   │
│   ├── schemas/
│   │   └── chat_schema.py
│   │
│   ├── services/
│   │   ├── document_service.py
│   │   ├── embedding_service.py
│   │   ├── retriever_service.py
│   │   └── rag_service.py
│   │
│   └── routes.py
│
├── uploads/
│
├── config.py
├── main.py
├── .env.example
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/rishurajgit/multi-format-rag.git

cd multi-format-rag
```

---

### Install Dependencies

```bash
uv sync
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
GEMINI_API_KEY=your_api_key

LLM_MODEL=gemini-2.5-flash

EMBEDDING_MODEL=gemini-embedding-2-preview

CHUNK_SIZE=1000
CHUNK_OVERLAP=200

CHROMA_DB_PATH=./chroma_db
UPLOAD_DIR=uploads
```

---

## Running the Application

```bash
uv run uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

### Upload PDF

**POST**

```
/upload
```

Uploads a PDF document, extracts text, creates embeddings, and stores the document in ChromaDB.

Example Response

```json
{
  "message": "PDF uploaded successfully",
  "document_name": "RAG Project 1.pdf",
  "total_pages": 3,
  "total_chunks": 6
}
```

---

### Chat

**POST**

```
/chat
```

Request

```json
{
  "question": "What is RAG?"
}
```

Example Response

```json
{
  "answer": "RAG stands for Retrieval-Augmented Generation...",
  "sources": [
    {
      "document_name": "RAG Project 1.pdf",
      "page": 1,
      "chunk_id": 3
    }
  ]
}
```

---

## Current Workflow

```text
PDF Upload
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
Gemini Embeddings
      │
      ▼
ChromaDB
      │
      ▼
Retriever
      │
      ▼
Prompt Template
      │
      ▼
Gemini LLM
      │
      ▼
Answer + Source Citation
```

---

## Current Limitations

- Currently supports PDF documents only.
- Conversation history is not maintained.
- Retrieval always returns the top matching chunks.
- Multiple document format support (DOCX, TXT, Markdown) is planned.

---

## Future Enhancements

- DOCX support
- TXT support
- Markdown support
- Similarity score threshold
- Streaming responses
- Conversation memory
- Multi-document collections
- Better citation formatting
- Docker

---

## Author

**Rishu Raj**

GitHub: https://github.com/rishurajgit