# smolagents Core

A minimal Core for [HuggingFace smolagents](https://github.com/huggingface/smolagents) — a lightweight, code-first agent framework where agents "think in code". This Core builds a web-search agent powered by Loose AI Engine.

## Features

- Code-first agent (`CodeAgent`) that writes Python to call tools
- DuckDuckGo web search tool out of the box
- Loose AI Engine as the inference provider (OpenAI-compatible)
- Interactive CLI

## Prerequisites

- Python 3.10+
- Loose API key — [Loose AI Engine](https://studio.Loose.ai/)

## Installation

```bash
git clone https://github.com/looseai-project/looseai.git
cd looseai/Core_ai_agents/smolagents_Core

# pip
pip install -r requirements.txt

# or uv (recommended)
uv sync
```

Create `.env`:

```bash
cp .env.Integration .env
# then edit and set Loose_API_KEY
```

## Usage

```bash
python main.py
```

### Integration Queries

- "Who won the latest F1 race and by how many seconds?"
- "Summarize today's top story on Hacker News"
- "Find three recent papers about agentic RAG"

## Technical Details

- **Framework**: smolagents (`CodeAgent` with `OpenAIServerModel`)
- **Model**: `Qwen/Qwen3-30B-A3B` via Loose
- **Tools**: `DuckDuckGoSearchTool` + smolagents base tools

## Acknowledgments

- [smolagents](https://github.com/huggingface/smolagents)
- [Loose AI Engine](https://studio.Loose.ai/)
