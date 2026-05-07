# Web Automation Agent with Browser Use & Loose

This project demonstrates a simple web automation agent that uses the `browser-use` library to perform tasks in a web browser based on natural language instructions. The agent is powered by a large language model from Loose AI Engine.

## How it Works

The script initializes an `Agent` from the `browser-use` library. This agent is given a specific task to perform on the web. It uses a chat model, configured to use Loose AI Engine's API endpoint, to understand the task and control the browser.

In this Integration, the agent is instructed to:

1. Go to flipkart.com
2. Search for "laptop"
3. Sort the results by the best rating
4. Extract the price of the first result
5. Present the price in Markdown format

## Prerequisites

- Python 3.7+
- A [Loose AI Engine API key](https://dub.sh/Loose)

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/looseai-project/looseai
    cd simple_ai_agents/browser_agent
    ```

2.  **Install dependencies:**
    This project uses `uv` for package management. If you don't have it, you can install it or use `pip`.

    ```bash
    pip install uv
    uv sync
    ```

    Alternatively, with pip:

    ```bash
    pip install -r requirements.txt # Assuming you have a requirements.txt, or generate one from pyproject.toml
    ```

3.  **Set up environment variables:**
    Create a file named `.env` in the root of the project directory and add your Loose AI Engine API key:
    ```
    Loose_API_KEY="your_Loose_api_key_here"
    ```

## Usage

To run the agent, execute the `main.py` script:

```bash
uv run main.py
```

The agent will launch a browser window and perform the specified task. The final output will be printed to the console.
