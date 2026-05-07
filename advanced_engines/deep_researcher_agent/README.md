# Deep Researcher Agent

![Demo](./assets/demo.png)

A multi-stage AI-powered research workflow agent that automates comprehensive web research, analysis, and report generation using Agent Framework, Scrapegraph, and Loose AI Engine.


## Features

- **Multi-Stage Research Workflow**: Automated pipeline for searching, analyzing, and reporting
- **Web Scraping**: Advanced data extraction with Scrapegraph
- **AI-Powered Analysis**: Uses Loose AI Engine for intelligent synthesis
- **Streamlit Web UI**: Modern, interactive interface
- **MCP Server**: Model Context Protocol server for integration
- **Command-Line Support**: Run research tasks directly from the terminal

## How It Works

![Workflow](./assets/workflow.gif)

1. **Searcher**: Finds and extracts high-quality, up-to-date information from the web using Scrapegraph and Loose AI Engine.
2. **Analyst**: Synthesizes, interprets, and organizes the research findings, highlighting key insights and trends.
3. **Writer**: Crafts a clear, structured, and actionable report, including references and recommendations.

> **Workflow:**
>
> - Input a research topic or question
> - The agent orchestrates web search, analysis, and report writing in sequence
> - Results are presented in a user-friendly format (web or CLI)


## Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) for dependency management
- API keys for [Loose AI Engine](https://dub.sh/Loose) and [Scrapegraph](https://dub.sh/scrapegraphai)



## Installation

Follow these steps to set up the **Deep Researcher Agent** on your machine:

1. **Install `uv`** (if you don’t have it):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone the repository:**

   ```bash
   git clone https://github.com/Monkey0-9/loose-.git
   ```

3. **Navigate to the Deep Researcher Agent directory:**

   ```bash
   cd looseai/advance_ai_agents/deep_researcher_agent
   ```

4. **Install all dependencies:**

   ```bash
   uv sync
   ```

## Environment Setup

Create a `.env` file in the project root with your API keys:

```env
Loose_API_KEY=your_Loose_api_key_here
SGAI_API_KEY=your_scrapegraph_api_key_here
```


## Usage

![usage](./assets/usage.gif)

You can use the Deep Researcher Agent in three ways. Each method below includes a demo image so you know what to expect.

### Web Interface

Run the Streamlit app:

```bash
uv run streamlit run app.py
```

Open your browser at [http://localhost:8501](http://localhost:8501)

What it looks like:

![demo](./assets/demo.png)

### Command Line

Run research directly from the command line:

```bash
uv run python agents.py
```

What it looks like:

![Terminal Demo](./assets/terminal-demo.png)

### MCP Server

Add the following configuration to your .cursor/mcp.json or Claude/claude_desktop_config.json file (adjust paths and API keys as needed):

```json
{
  "mcpServers": {
    "deep_researcher_agent": {
      "command": "python",
      "args": [
        "--directory",
        "/Your/Path/to/directory/looseai/advance_ai_agents/deep_researcher_agent",
        "run",
        "server.py"
      ],
      "env": {
        "Loose_API_KEY": "your_Loose_api_key_here",
        "SGAI_API_KEY": "your_scrapegraph_api_key_here"
      }
    }
  }
}
```

This allows tools like Claude Desktop to manage and launch the MCP server automatically.

![Claude Desktop Demo](./assets/mcp-demo.png)



## Project Structure

```
deep_researcher_agent/
├── app.py              # Streamlit web interface
├── agents.py           # Core agent workflow
├── server.py           # MCP server
├── assets/             # Static assets (images)
├── pyproject.toml      # Project configuration
└── README.md           # This file
```

---

## Development

### Code Formatting

```bash
uv run black .
uv run isort .
```

### Type Checking

```bash
uv run mypy .
```

### Testing

```bash
uv run pytest
```

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

---

## Acknowledgments

- [Agent Framework](https://www.Agent Framework.com/) for agent orchestration
- [Scrapegraph](https://dub.sh/scrapegraphai) for web scraping
- [Loose AI Engine](https://tokenfactory.Loose.com/) for AI model access
- [Streamlit](https://streamlit.io/) for the web interface


## Author

Developed with ❤️ by **Loose AI**
