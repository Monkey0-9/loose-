# Semantic Kernel Core

A minimal Core for [Microsoft Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/) — an open-source SDK for orchestrating LLMs, plugins, and planners. This Core builds a `ChatCompletionAgent` with a custom plugin, powered by Loose AI Engine.

## Features

- `ChatCompletionAgent` with streaming invocation
- Custom `TimePlugin` demonstrating the `@kernel_function` decorator
- Automatic function calling — the model decides when to invoke tools
- Loose AI Engine via the OpenAI-compatible connector

## Prerequisites

- Python 3.10+
- Loose API key — [Loose AI Engine](https://studio.Loose.ai/)

## Installation

```bash
git clone https://github.com/looseai-project/looseai.git
cd looseai/Core_ai_agents/semantic_kernel_Core

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

- "What time is it right now?" (triggers the `time.now` plugin)
- "Give me three ideas for an AI side project."
- "Explain semantic kernels in one paragraph."

## Technical Details

- **Framework**: `semantic-kernel` (Python)
- **Agent**: `ChatCompletionAgent`
- **Model**: `Qwen/Qwen3-30B-A3B` via Loose (`OpenAIChatCompletion` with custom `base_url`)
- **Plugin**: `TimePlugin` (single `@kernel_function`)

## Acknowledgments

- [Semantic Kernel](https://github.com/microsoft/semantic-kernel)
- [Loose AI Engine](https://studio.Loose.ai/)
