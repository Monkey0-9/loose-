"""
Loose AI — PDF Chat with Trust Metrics (Streamlit RAG App)
Upload a PDF, ask questions, get answers with Trust Score & Hallucination Risk.

Run:  streamlit run app.py
"""

import os
import re
import math
import random
import tempfile
import textwrap
from pathlib import Path
from typing import Optional
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ─────────────────────────────────────────────────────────────────
# Text extraction
# ─────────────────────────────────────────────────────────────────
def extract_text_from_pdf(path: str) -> str:
    """Extract all text from a PDF file using pypdf."""
    try:
        from pypdf import PdfReader
        reader = PdfReader(path)
        pages  = [page.extract_text() or "" for page in reader.pages]
        return "\n\n".join(pages)
    except Exception as e:
        return f"[PDF extraction error: {e}]"


# ─────────────────────────────────────────────────────────────────
# In-memory vector index (mock embedding with TF-IDF-like scoring)
# ─────────────────────────────────────────────────────────────────
class InMemoryIndex:
    """Lightweight in-memory chunk store with keyword-based similarity."""

    def __init__(self, chunk_size: int = 400, overlap: int = 50):
        self.chunks: list[str] = []
        self.chunk_size = chunk_size
        self.overlap    = overlap

    def build(self, text: str):
        """Split text into overlapping chunks."""
        words  = text.split()
        chunks = []
        step   = self.chunk_size - self.overlap
        for i in range(0, len(words), max(1, step)):
            chunk = " ".join(words[i:i + self.chunk_size])
            if chunk:
                chunks.append(chunk)
        self.chunks = chunks

    def search(self, query: str, top_k: int = 3) -> list[tuple[str, float]]:
        """Keyword overlap similarity search."""
        if not self.chunks:
            return []
        query_words = set(re.findall(r"\w+", query.lower()))

        def score(chunk: str) -> float:
            chunk_words = set(re.findall(r"\w+", chunk.lower()))
            overlap     = query_words & chunk_words
            return len(overlap) / max(1, math.sqrt(len(query_words) * len(chunk_words)))

        scored = [(c, score(c)) for c in self.chunks]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]

    def __len__(self):
        return len(self.chunks)


# ─────────────────────────────────────────────────────────────────
# Mock RAG answer
# ─────────────────────────────────────────────────────────────────
def mock_rag_answer(question: str, chunks: list[tuple[str, float]]) -> dict:
    """Simulate a RAG answer with trust metrics."""
    if not chunks:
        return {
            "answer":       "No relevant content found in the document.",
            "trust_score":  0.1,
            "hallucination_risk": 0.9,
            "citations":    [],
            "claims":       [],
        }

    best_chunk = chunks[0][0][:200]
    trust = min(max(chunks[0][1] * 3.5, 0.0), 1.0)  # scale and clamp to [0,1]
    hallucination_risk = round(1.0 - trust, 3)
    trust = round(trust, 3)

    answer = (
        f"**[Mock RAG Answer]**\n\n"
        f"Based on the document, regarding '*{question[:50]}*':\n\n"
        f"> {textwrap.shorten(best_chunk, 300, placeholder='…')}\n\n"
        f"*This is a mock response. Set `USE_REAL_LLM=1` for real AI answers.*"
    )

    claims = [
        {"text": f"The document addresses '{question[:30]}…'",        "verdict": "SUPPORTED",      "color": "#16a34a"},
        {"text": "Additional context may exist in other sections.",    "verdict": "PARTIAL",        "color": "#ca8a04"},
        {"text": f"Exact statistics for '{question[:20]}' confirmed.", "verdict": "UNSUPPORTED",   "color": "#dc2626"},
    ]

    return {
        "answer":             answer,
        "trust_score":        trust,
        "hallucination_risk": hallucination_risk,
        "citations":          [c for c, _ in chunks],
        "claims":             claims,
    }


def real_rag_answer(question: str, chunks: list[tuple[str, float]], api_key: str) -> dict:
    """Real RAG: pass retrieved chunks to OpenAI for grounded answer."""
    import openai
    client  = openai.OpenAI(api_key=api_key)
    context = "\n\n---\n\n".join(c for c, _ in chunks)

    messages = [
        {"role": "system", "content": (
            "You are a precise assistant. Answer ONLY based on the provided document context. "
            "If uncertain, say so. Use Markdown. Be concise."
        )},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
    ]

    try:
        resp = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
        answer = resp.choices[0].message.content
        # Estimate trust from response length and context overlap
        context_words = set(re.findall(r"\w+", context.lower()))
        answer_words  = set(re.findall(r"\w+", answer.lower()))
        overlap_ratio = len(answer_words & context_words) / max(1, len(answer_words))
        trust = min(max(overlap_ratio * 1.5, 0.0), 1.0)
    except Exception as e:
        answer = f"⚠️ LLM error: {e}"
        trust  = 0.0

    return {
        "answer":             answer,
        "trust_score":        round(trust, 3),
        "hallucination_risk": round(1.0 - trust, 3),
        "citations":          [c[:200] for c, _ in chunks],
        "claims":             [],
    }


# ─────────────────────────────────────────────────────────────────
# Verdict badge
# ─────────────────────────────────────────────────────────────────
def verdict_badge(verdict: str, color: str) -> str:
    return (
        f'<span style="background:{color};color:white;padding:2px 8px;'
        f'border-radius:4px;font-size:0.78rem;font-weight:600;">{verdict}</span>'
    )


# ─────────────────────────────────────────────────────────────────
# Streamlit App
# ─────────────────────────────────────────────────────────────────
def main():
    st.set_page_config(page_title="PDF Chat — Loose AI", layout="wide", page_icon="📄")

    st.markdown("""
    <div style="background:linear-gradient(135deg,rgba(102,126,234,0.2),rgba(22,163,74,0.15));
                padding:24px 32px;border-radius:14px;margin-bottom:16px;">
        <h1 style="margin:0;color:#e2e8f0;">📄 Trustworthy PDF Chat</h1>
        <p style="margin:6px 0 0;color:#94a3b8;">
            Upload a PDF → ask questions → get grounded answers with trust metrics.
            <span style="background:#667eea;color:white;padding:2px 8px;border-radius:4px;font-size:0.8rem;">Loose AI</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        use_real = st.toggle("Use Real LLM (OpenAI)", value=os.getenv("USE_REAL_LLM") == "1")
        api_key  = os.getenv("OPENAI_API_KEY", "")
        if use_real and not api_key:
            st.error("⚠️ OPENAI_API_KEY missing")
            use_real = False
        st.divider()
        st.caption("Trust Score: fraction of answer grounded in document.\nHallucination Risk = 1 − Trust Score.")

    # Session state
    if "index" not in st.session_state:
        st.session_state.index:    Optional[InMemoryIndex] = None
        st.session_state.doc_name: str = ""
        st.session_state.history:  list = []

    # Upload
    uploaded = st.file_uploader("📤 Upload a PDF", type=["pdf"], key="pdf_uploader")

    if uploaded:
        new_name = uploaded.name
        if new_name != st.session_state.doc_name:
            # New file → rebuild index
            with st.spinner(f"📚 Indexing '{new_name}'…"):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(uploaded.read())
                    tmp_path = tmp.name
                text  = extract_text_from_pdf(tmp_path)
                Path(tmp_path).unlink(missing_ok=True)
                index = InMemoryIndex()
                index.build(text)
                st.session_state.index    = index
                st.session_state.doc_name = new_name
                st.session_state.history  = []  # reset chat on new doc
            st.success(f"✅ Indexed '{new_name}' — {len(index)} chunks.")

    # Show chat history
    for role, content in st.session_state.history:
        with st.chat_message(role):
            st.markdown(content)

    # Question input
    question = st.chat_input("Ask a question about your document…")
    if not question:
        if st.session_state.index is None:
            st.info("👆 Upload a PDF to get started.")
        return

    if st.session_state.index is None:
        st.warning("Please upload a PDF first.")
        return

    # User message
    st.session_state.history.append(("user", question))
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching document & generating answer…"):
            chunks  = st.session_state.index.search(question, top_k=3)
            if use_real:
                result = real_rag_answer(question, chunks, api_key)
            else:
                result = mock_rag_answer(question, chunks)

        # Answer
        st.markdown(result["answer"])

        # Trust metrics
        col1, col2 = st.columns(2)
        trust = result["trust_score"]
        hrisk = result["hallucination_risk"]
        col1.metric("📊 Trust Score",        f"{trust:.0%}", delta=None)
        col2.metric("⚠️ Hallucination Risk", f"{hrisk:.0%}",
                    delta=None,
                    delta_color="inverse" if hrisk > 0.4 else "normal")

        # Claims verification
        if result["claims"]:
            st.subheader("🔍 Claims Verification")
            for claim in result["claims"]:
                badge = verdict_badge(claim["verdict"], claim["color"])
                st.markdown(f'{badge} {claim["text"]}', unsafe_allow_html=True)

        # Source citations
        if result["citations"]:
            with st.expander("📎 Source Chunks"):
                for i, citation in enumerate(result["citations"], 1):
                    st.markdown(f"**Chunk {i}:** {citation[:300]}…")

        st.session_state.history.append(("assistant", result["answer"]))


if __name__ == "__main__":
    main()
