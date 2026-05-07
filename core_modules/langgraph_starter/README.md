# LangGraph Core

A minimal Core for [LangGraph](https://langchain-ai.github.io/langgraph/) — a framework for building stateful, graph-based LLM applications. This Core uses the prebuilt `create_react_agent` to assemble a ReAct loop (reason → act → observe) powered by Loose AI Engine.

## Features

- Prebuilt ReAct agent from `langgraph.prebuilt.create_react_agent`
- Two Python tools auto-called by the model: `get_current_time`, `word_count`
- Multi-turn conversation via the graph's `messages` state
- Loose AI Engine via `ChatOpenAI` (OpenAI-compatible)

## Prerequisites

- Python 3.10+
- Loose API key — [Loose AI Engine](https://studio.Loose.ai/)

## Installation

```bash
git clone https://github.com/looseai-project/looseai.git
cd looseai/Core_ai_agents/langgraph_Core

pip install -r requirements.txt
# or: uv sync
```

Create `.env`:

```bash
cp .env.Integration .env
# set Loose_API_KEY
```

## Usage

```bash
python main.py
```

### Integration Queries

- "What time is it right now?" (triggers `get_current_time`)
- "How many words are in 'the quick brown fox jumps'?" (triggers `word_count`)
- "Explain the ReAct pattern in two sentences."

## Technical Details

- **Framework**: `langgraph` + `langchain-openai`
- **Agent**: `create_react_agent` (prebuilt ReAct loop — reason, act, observe)
- **Model**: `Qwen/Qwen3-30B-A3B` via Loose (`ChatOpenAI` with custom `base_url`)
- **Tools**: `get_current_time`, `word_count` (plain `@tool`-decorated functions)

## Next Steps

To move beyond the prebuilt agent, define your own `StateGraph` with explicit `nodes` and `edges` so you can control routing, add memory, or branch on tool results. See the [LangGraph docs](https://langchain-ai.github.io/langgraph/) for building from scratch.

## Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Loose AI Engine](https://studio.Loose.ai/)
