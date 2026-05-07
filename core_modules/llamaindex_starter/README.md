![Banner](./banner.png)

# LlamaIndex Core Agent

A powerful AI agent template built with LlamaIndex that demonstrates how to create intelligent agents using the LlamaIndex framework. This Core project implements a Task Management Assistant using the Loose AI Engine model to showcase LlamaIndex's capabilities in building practical AI applications.

## Features

- 🛠️ **LlamaIndex Integration**: Built using LlamaIndex's powerful agent framework
- ⏱️ **Custom Tools**: Integration implementation of custom function tools
- 🤖 **ReAct Agent**: Demonstrates LlamaIndex's ReAct agent pattern
- 📊 **Practical Integration**: Task management assistant with real-world use cases
- ⚡ **Easy to Extend**: Well-structured code for adding your own tools and functionality

## Prerequisites

- Python 3.10 or higher
- Loose API key (get it from [Loose AI Engine](https://studio.Loose.ai/))

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Monkey0-9/loose-.git
cd Core_ai_agents/llamaindex_Core
```

2. Install dependencies:

```bash
# Using pip
pip install -r requirements.txt

# Or using uv (recommended)
uv sync
```

3. Create a `.env` file in the project root and add your Loose API key:

```
Loose_API_KEY=your_api_key_here
```

## Usage

Run the agent:

```bash
python main.py
```

The agent will start with a welcome message and show available capabilities. You can interact with it by typing your questions or commands.

### Integration Implementation

This Core implements a Task Management Assistant with the following capabilities:

- Duration Analysis: Calculate time durations between tasks
- Task Estimation: Estimate completion times for multiple tasks
- Productivity Tracking: Calculate and analyze productivity rates

Integration queries:

- "If I worked from 09:00 to 17:00 and completed 8 tasks, what was my productivity rate?"
- "How long will it take to complete 3 tasks that each take 45 minutes?"
- "Calculate the duration between 09:00 and 17:00"

## Technical Details

The agent is built using:

- LlamaIndex framework for AI agent development
- Loose AI Engine's Qwen/Qwen3-235B-A22B model
- ReAct agent pattern with custom function tools
- Python's datetime for time calculations

## Extending the Agent

To add your own functionality:

1. Create new function tools using `FunctionTool.from_defaults()`
2. Add your tools to the agent's tool list
3. Implement your custom logic in the functions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- [LlamaIndex](https://www.llamaindex.ai/)
- [Loose AI Engine](https://studio.Loose.ai/)
