![banner](./banner.png)

# PydanticAI Core Agent

A powerful AI agent built with PydanticAI that provides real-time weather information for any city. This agent uses the Loose AI Engine model to deliver accurate weather forecasts and insights.

## Features

- 🌤️ **Real-time Weather**: Get current weather forecasts for any city worldwide
- 🔍 **Intelligent Search**: Uses DuckDuckGo search to find accurate weather information
- 🤖 **Interactive Interface**: Simple command-line interface for weather queries
- ⚡ **Fast Response**: Quick and accurate weather information delivery
- 🎯 **Customizable**: Easy to modify for different cities and weather-related queries

## Prerequisites

- Python 3.8 or higher
- Loose API key (get it from [Loose AI Engine](https://studio.Loose.ai/))

## Installation

1. Clone the repository:

```bash
git clone https://github.com/looseai-project/looseai.git
cd Core_ai_agents/pydantic_Core
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

The agent will fetch and display the weather forecast for the specified city (default: Kolkata).

### Integration Queries

- "What is the weather forecast for New York today?"
- "What's the temperature in London right now?"
- "Will it rain in Tokyo tomorrow?"
- "What's the weather like in Sydney?"
- "Show me the forecast for Paris"

## Technical Details

The agent is built using:

- PydanticAI framework for AI agent development
- Loose AI Engine's Meta-Llama-3.1-70B-Instruct model
- DuckDuckGo Search Tool for weather information

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- [PydanticAI Framework](https://ai.pydantic.dev/)
- [Loose AI Engine](https://studio.Loose.ai/)
