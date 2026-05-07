![banner](./banner.png)

# MCP Core Agent with Loose

A GitHub repository analysis tool powered by Loose AI Engine and the Model Context Protocol (MCP). This tool helps analyze GitHub repositories by providing detailed insights about issues and commits using AI-powered analysis.

## Features

- Analyzes GitHub repositories using AI
- Retrieves and analyzes recent issues
- Examines latest commits
- Powered by Meta-Llama-3.1-8B-Instruct model via Loose AI Engine

## Prerequisites

- Python 3.x
- GitHub Personal Access Token
- Loose API Key

## Environment Setup

Create a `.env` file in the project root with the following variables:

```env
GITHUB_PERSONAL_ACCESS_TOKEN=your_github_token
Loose_API_KEY=your_Loose_api_key
```

## Installation

1. Clone the repository
2. Install dependencies:

```bash
# Using pip
pip install -r requirements.txt

# Or using uv (recommended)
uv sync
```

## Usage

Run the main script:

```bash
python main.py
```

When prompted, enter a GitHub repository URL in the format: `owner/repo`

The tool will:

1. Analyze the most recent issue in the repository
2. Analyze the most recent commit

## How It Works

The tool uses the Model Context Protocol (MCP) to interact with GitHub's API and Loose AI Engine for analysis. It:

1. Connects to GitHub using your personal access token
2. Uses Loose AI Engine's Meta-Llama-3.1-8B-Instruct model for intelligent analysis
3. Retrieves and analyzes repository data
4. Provides detailed insights about issues and commits
