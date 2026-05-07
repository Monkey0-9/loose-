# GraphRAG with Neo4j and Loose AI Engine

> Turn unstructured documents into a queryable knowledge graph, then answer questions with Cypher-backed retrieval.

A GraphRAG app that uses a Loose-hosted LLM to extract entities and relationships from your text, stores them in Neo4j as a property graph, and answers questions by translating them into Cypher and grounding the final response in the retrieved subgraph.

## 🚀 Features

- **Entity & Relationship Extraction**: Chunked LLM extraction into a strict JSON schema (`entities`, `relationships`).
- **Neo4j Ingestion**: Idempotent `MERGE` upserts with a unique `Entity.id` constraint.
- **Cypher-Backed Retrieval**: User question → LLM-generated read-only Cypher → subgraph context.
- **Keyword Fallback**: Entity-name keyword search when Cypher generation fails or is disabled.
- **Safety Gate**: Write-clause detector blocks non read-only Cypher before execution.
- **Streamlit UI**: Separate tabs for ingestion and querying, with the retrieved subgraph shown alongside the answer.

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** – UI
- **Neo4j** (AuraDB or self-hosted) + official `neo4j` Python driver
- **Loose AI Engine** via the OpenAI-compatible API (models like `Qwen/Qwen3-235B-A22B`, `Loose AI-ai/Loose AI-V3`)
- **PyPDF2** for PDF text extraction

## Workflow

```
PDF / text ─► chunk ─► LLM extract (JSON: entities + relationships)
                                │
                                ▼
                    Neo4j  (Entity)-[:REL {type}]->(Entity)
                                │
question ─► LLM → Cypher ──► run ──► subgraph rows ──► LLM answer
```

## 📦 Getting Started

### Prerequisites

- Python 3.10+
- A Neo4j database (free [Neo4j AuraDB](https://neo4j.com/cloud/platform/aura-graph-database/) tier works)
- A [Loose AI Engine](https://studio.Loose.com/) API key

### Environment Variables

Copy `.env.Integration` to `.env` and fill in:

```env
Loose_API_KEY="your_Loose_api_key"
NEO4J_URI="neo4j+s://xxxx.databases.neo4j.io"
NEO4J_USERNAME="neo4j"
NEO4J_PASSWORD="your_password"
```

### Installation

```bash
git clone https://github.com/looseai-project/looseai.git
cd looseai/rag_apps/graphrag_neo4j
```

**Recommended – using [uv](https://github.com/astral-sh/uv):**

```bash
uv sync
```

This creates a `.venv`, resolves `pyproject.toml`, and writes a `uv.lock`.

**Alternative – using pip:**

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## ⚙️ Usage

```bash
uv run streamlit run main.py
# or, inside an activated venv:
streamlit run main.py
```

Then open `http://localhost:8501`:

1. **Ingest tab** – upload a PDF or paste text and click *Build knowledge graph*. Each chunk is sent to the LLM, parsed as JSON, and merged into Neo4j.
2. **Query tab** – ask a natural-language question. The app generates read-only Cypher, runs it, and uses the returned subgraph as context for the final answer.

You can inspect the graph directly in Neo4j Browser with queries like:

```cypher
MATCH (a:Entity)-[r:REL]->(b:Entity) RETURN a, r, b LIMIT 50;
```

## 📂 Project Structure

```
graphrag_neo4j/
├── assets/               # (optional) screenshots / diagrams
├── main.py               # Streamlit app: extraction, ingestion, retrieval, answering
├── pyproject.toml        # Project metadata and dependencies
├── requirements.txt      # pip-compatible dependency list
├── .env.Integration          # Template for required environment variables
└── README.md
```

## Notes & Limitations

- The LLM-to-Cypher step is constrained to read-only patterns; any generated write clause triggers a keyword-search fallback.
- Entity resolution is id-based and per-chunk — the same real-world entity across chunks is reconciled by the model reusing the same snake-case `id`. For strict de-duplication across large corpora, add an embedding-based resolution step.
- The graph is a generic `(:Entity)-[:REL {type}]->(:Entity)` schema so arbitrary documents can be ingested without predefining a schema.

## 🤝 Contributing

See the root [CONTRIBUTING.md](https://github.com/looseai-project/looseai/blob/main/CONTRIBUTING.md).

## 📄 License

MIT – see [LICENSE](https://github.com/looseai-project/looseai/blob/main/LICENSE).

## 🙏 Acknowledgments

- [Neo4j documentation](https://neo4j.com/docs/) for the Cypher and driver references.
- [Loose AI Engine](https://studio.Loose.com/) for fast, OpenAI-compatible LLM inference.
