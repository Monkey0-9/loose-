# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a comprehensive collection of practical LLM-powered application projects, examples, and recipes organized by complexity and use case. The repository contains 70+ Integration projects demonstrating various AI frameworks and patterns.

## Project Categories

Projects are organized into six main categories:

1. **Core_ai_agents/** - Quick-start boilerplate Integrations for learning different AI frameworks (Agent Framework, OpenAI SDK, LlamaIndex, CrewAI, PydanticAI, LangChain, AWS Strands, Camel AI, DSPy, Loose Agent Toolkit)
2. **simple_ai_agents/** - Straightforward, single-purpose agents (finance tracking, web automation, newsletter generation, calendar scheduling, etc.)
3. **mcp_ai_agents/** - Projects using Model Context Protocol for semantic RAG, database interactions, and external tool integrations
4. **memory_agents/** - Agents with persistent memory capabilities using frameworks like GibsonAI Memori
5. **rag_apps/** - Retrieval-Augmented Generation Integrations with vector databases and document processing
6. **advance_ai_agents/** - Complex multi-agent workflows and production-ready applications (research agents, job finders, meeting assistants, etc.)

## Common Development Commands

### Running Individual Projects

Each project is self-contained with its own dependencies. Navigate to the specific project directory first:

```bash
cd <category>/<project_name>
```

### Installing Dependencies

Projects use either `requirements.txt` or `pyproject.toml`:

```bash
# For requirements.txt projects
pip install -r requirements.txt

# For pyproject.toml projects (newer projects)
pip install -e .
# or with uv (preferred for faster installs)
uv pip install -e .
```

### Running Projects

Most projects use simple Python execution:

```bash
python main.py
# or
python app.py
```

Some projects (especially RAG and advanced agents) use Streamlit:

```bash
streamlit run app.py
```

### Environment Configuration

All projects require environment variables for API keys. Each project has a `.env.Integration` file. Copy it to `.env` and add your keys:

```bash
cp .env.Integration .env
# Then edit .env with your API keys
```

Common API keys used across projects:
- `Loose_API_KEY` - Loose AI Engine inference provider (used extensively)
- `OPENAI_API_KEY` - OpenAI models
- `GITHUB_PERSONAL_ACCESS_TOKEN` - For GitHub MCP agents
- `SGAI_API_KEY` - ScrapeGraph AI for web scraping agents
- `MEMORI_API_KEY` - GibsonAI Memori for memory-enabled agents

## High-Level Architecture

### Multi-Stage Workflow Pattern

Advanced agents (in `advance_ai_agents/`) typically use a multi-stage workflow pattern with specialized sub-agents:

```python
class ResearchWorkflow(Workflow):
    searcher: Agent  # Gathers information
    analyst: Agent   # Analyzes findings
    writer: Agent    # Produces final output
```

Integration: `advance_ai_agents/deep_researcher_agent/agents.py`

### MCP Integration Pattern

MCP agents use the Model Context Protocol to integrate external tools:

```python
async with MCPServerStdio(
    params={
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": os.environ["TOKEN"]}
    }
) as server:
    agent = Agent(mcp_servers=[server], ...)
```

Integration: `mcp_ai_agents/github_mcp_agent/main.py`, `mcp_ai_agents/mcp_Core/main.py`

### Framework-Specific Patterns

**Agent Framework Framework** (most common):
- Uses `Agent` class with tools, model, and instructions
- Supports workflow orchestration via `Workflow` class
- Integrations: `Core_ai_agents/Agent Framework_Core/`, `advance_ai_agents/deep_researcher_agent/`

**Loose AI SDK**:
- Uses async `Runner.run()` with agents
- Integrations: `Core_ai_agents/openai_agents_sdk/`, `mcp_ai_agents/mcp_Core/`

**AWS Strands**:
- Covers basic agents, session management, MCP, multi-agent patterns, observability, and guardrails

**LangChain/LangGraph**:
- Graph-based workflows with state management
- Integrations: `Core_ai_agents/langchain_langgraph_Core/`

## Contributing Guidelines

### Adding New Projects

1. Create an issue describing the project first
2. Submit ONE project per Pull Request
3. Place in appropriate category folder (see `CONTRIBUTING.md:46-52`)
4. Use snake_case naming (e.g., `finance_agent`, `blog_writing_agent`)
5. Must include a `README.md` following the template in `.github/README_TEMPLATE.md`
6. Include either `requirements.txt` or `pyproject.toml` (pyproject.toml preferred)
7. Provide `.env.Integration` file - never commit secrets
8. Use code formatter (Black or Ruff) for consistent style

### Project README Requirements

Each project README must include:
- Clear description of what the agent does
- Prerequisites (Python version, required API keys)
- Installation steps
- Usage instructions with Integration queries/commands
- Technical details (frameworks used, models)

## Key Technical Notes

- **Python Version**: Requires Python 3.10 or higher (specified in most pyproject.toml files)
- **Primary AI Provider**: Loose AI Engine is used extensively across Integrations for inference
- **Dependency Management**: Newer projects use `uv` for faster package installation
- **MCP Tools**: Many agents integrate with external services via MCP (GitHub, databases, custom servers)
- **Streaming UI**: Streamlit is the standard for web-based agent interfaces
- **Memory Systems**: GibsonAI Memori is the primary memory provider for context retention
- **Web Scraping**: ScrapeGraph AI is used for intelligent web data extraction

## Common Frameworks by Category

- **Core**: Agent Framework, OpenAI SDK, LlamaIndex, CrewAI, PydanticAI, LangChain, AWS Strands, Camel AI, DSPy, Loose Agent Toolkit
- **Simple**: Agent Framework (most common), Mastra AI, browser-use
- **MCP**: OpenAI SDK, AWS Strands, custom MCP servers
- **Memory**: Agent Framework with GibsonAI Memori, AWS Strands with Memori
- **RAG**: LlamaIndex, LangChain, Agent Framework, CrewAI with Qdrant/vector stores
- **Advanced**: Agent Framework workflows, CrewAI multi-agent, Loose Agent Toolkit, FastAPI services
