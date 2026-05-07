# PDF Chat — Trustworthy RAG App (Loose AI)

A Streamlit app where you upload a PDF, it's indexed, and you chat with it — with **Trust Score** and **Hallucination Risk** metrics.

## Features
- 📄 PDF upload and in-memory indexing
- 💬 Chat with Q&A over your document
- 📊 Trust Score (0–1) and Hallucination Risk metrics
- ✅ Per-claim verification (Supported / Contradicted)
- Mocked by default (no vector DB or real LLM needed)

## Setup

```bash
pip install -r requirements.txt
cp .env.Integration .env
streamlit run app.py
```

## Real Mode

```env
USE_REAL_LLM=1        # Use real OpenAI
OPENAI_API_KEY=sk-... 
USE_REAL_VECTOR_DB=1  # Use real Qdrant (docker run -p 6333:6333 qdrant/qdrant)
QDRANT_URL=http://localhost:6333
```

## Architecture

```
PDF Upload → Text Extraction → Chunking → Vector Index (in-memory)
                                               ↓
User Query → Similarity Search → Retrieved Chunks → LLM → Answer + Trust Metrics
```
