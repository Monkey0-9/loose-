# AutoGen Core

A minimal Core for [Microsoft AutoGen](https://microsoft.github.io/autogen/) — a framework for building multi-agent AI applications. This Core creates an `AssistantAgent` with a custom tool, powered by Loose AI Engine.

## Features

- `AssistantAgent` from `autogen-agentchat`
- Custom Python tool (`get_current_time`) auto-called by the model
- Streaming responses rendered via `Console`
- Loose AI Engine via `OpenAIChatCompletionClient` (OpenAI-compatible)

## Prerequisites

- Python 3.10+
- Loose API key — [Loose AI Engine](https://studio.Loose.ai/)

## Installation

```bash
git clone https://github.com/looseai-project/looseai.git
cd looseai/Core_ai_agents/autogen_Core

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

- "What time is it right now?" (triggers the `get_current_time` tool)
- "Write a haiku about distributed systems."
- "Explain multi-agent orchestration in one paragraph."

## Technical Details

- **Framework**: `autogen-agentchat` + `autogen-ext[openai]` (v0.4+)
- **Agent**: `AssistantAgent` with `reflect_on_tool_use=True`
- **Model**: `Qwen/Qwen3-30B-A3B` via Loose (`OpenAIChatCompletionClient` with custom `base_url`)
- **Tool**: `get_current_time` (plain Python function)

## Acknowledgments

- [AutoGen](https://github.com/microsoft/autogen)
- [Loose AI Engine](https://studio.Loose.ai/)
