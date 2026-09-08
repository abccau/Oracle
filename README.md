# Oracle

A production-style Enterprise Retrieval-Augmented Generation (RAG) system built using open-source models, LangChain, and Qdrant.

The project ingests enterprise documents, chunks them intelligently, generates embeddings, stores them in a vector database, and retrieves relevant context for answering user queries.

---

## Features

- Multi-document ingestion
- Recursive text chunking
- Metadata preservation
- Open-source embeddings
- Qdrant vector database
- Semantic similarity search
- Enterprise document retrieval
- Extensible RAG architecture

---

## Tech Stack

### Frameworks

- LangChain
- LangChain Community
- LangChain Text Splitters

### Embeddings

- BAAI/bge-small-en-v1.5

### Vector Database

- Qdrant

### LLM

- Open-source LLM (to be integrated)

### Language

- Python 3.11+

---

## Project Structure

```text
Oracle/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── ingestion/
│   ├── __init__.py
│   ├── loader.py
│   └── chunker.py
│
├── embeddings/
│   ├── __init__.py
│   └── embedder.py
│
├── qdrant/
│   ├── __init__.py
│   └── vectordb.py
│
├── retrieval/
│   ├── __init__.py
│   └── retriever.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Current Pipeline

```text
Documents
    ↓
Loader
    ↓
Chunker
    ↓
Embeddings
    ↓
Qdrant
    ↓
Retriever
    ↓
LLM
    ↓
Answer
```

---

## Dataset

The project uses a multi-company enterprise corpus containing:

- PDFs
- DOCX files
- HTML documents
- Policies
- Employee handbooks
- Product documentation
- Knowledge-base articles

Example:

```text
datasets/
│
├── Velvera Technologies/
│   ├── pdf/
│   ├── docx/
│   └── html/
│
├── ZX Bank/
│   ├── pdf/
│   ├── docx/
│   └── html/
│
└── ...
```

---

## Ingestion

### Loader

Responsible for:

- Discovering company folders
- Loading PDF documents
- Extracting text
- Preserving metadata

Metadata stored:

```python
{
    "company": "Velvera Technologies",
    "source": ".../Employee Handbook.pdf",
    "page": 0
}
```

---

### Chunking

Uses:

```python
RecursiveCharacterTextSplitter
```

Configuration:

```python
chunk_size = 1000
chunk_overlap = 200
```

Benefits:

- Maintains context continuity
- Improves retrieval accuracy
- Reduces information loss

---

## Embeddings

Model:

```text
BAAI/bge-small-en-v1.5
```

Advantages:

- Lightweight
- Fast inference
- High retrieval quality
- Works well with Qdrant
- Open-source

---

## Vector Database

Qdrant is used for:

- Vector storage
- Similarity search
- Metadata filtering
- Enterprise-scale retrieval

Example metadata filter:

```python
company = "ZX Bank"
```

---

## Retrieval Strategy

Current:

- Dense vector retrieval

Planned:

- Hybrid search
- Metadata filtering
- Reranking
- Parent-child retrieval

---

## Installation

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

### Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running

From project root:

```bash
python -m app.main
```

---

## Roadmap

### Phase 1

- [x] PDF ingestion
- [x] Recursive chunking

### Phase 2

- [ ] BGE embeddings
- [ ] Qdrant integration
- [ ] Similarity search

### Phase 3

- [ ] Retrieval pipeline
- [ ] Context construction
- [ ] Prompt engineering

### Phase 4

- [ ] Open-source LLM integration
- [ ] End-to-end RAG

### Phase 5

- [ ] Hybrid Search
- [ ] Reranking
- [ ] Parent-child Retrieval
- [ ] FastAPI service
- [ ] Docker deployment

---

## Future Enhancements

- Multi-format ingestion
- GraphRAG
- Agentic RAG
- Query rewriting
- Multi-query retrieval
- RAG Fusion
- Self-RAG
- Multi-vector retrieval
- Knowledge graph integration

---

## Author

Nidhish

Engineering Student, FAMT Ratnagiri

Enterprise RAG & Agentic AI Project