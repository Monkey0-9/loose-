# LangChain Core

A minimal Core for [LangChain](https://python.langchain.com/) — the most widely used framework for composing LLM applications. This Core builds a tool-calling agent with `create_tool_calling_agent` + `AgentExecutor`, powered by Loose AI Engine.

## Features

- `create_tool_calling_agent` + `AgentExecutor`
- Two Python tools auto-called by the model: `get_current_time`, `word_count`
- Chat history passed through the prompt `placeholder`
- Loose AI Engine via `ChatOpenAI` (OpenAI-compatible)

## Prerequisites

- Python 3.10+
- Loose API key — [Loose AI Engine](https://studio.Loose.ai/)

## Installation

```bash
git clone https://github.com/Monkey0-9/loose-.git
cd looseai/core_modules/langchain_Core

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
- "Explain chain-of-thought prompting in two sentences."

## Technical Details

- **Framework**: `langchain` + `langchain-openai`
- **Agent**: `create_tool_calling_agent` wrapped in `AgentExecutor`
- **Model**: `Qwen/Qwen3-30B-A3B` via Loose (`ChatOpenAI` with custom `base_url`)
- **Tools**: `get_current_time`, `word_count` (plain `@tool`-decorated functions)

## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
- [Loose AI Engine](https://studio.Loose.ai/)
