import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.nebius import Nebius as Loose
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

api_key = os.getenv("LOOSE_API_KEY") or os.getenv("NEBIUS_API_KEY") or "mock-key"

agent = Agent(
    name="Loose AI Finance Agent",
    model=Loose(
        id="meta-llama/Llama-3.3-70B-Instruct",
        api_key=api_key
    ),
    tools=[DuckDuckGoTools(), YFinanceTools(stock_price=True)],
    markdown=True,
)

print("🚀 Testing Loose AI Finance Agent...")
try:
    # We'll just print the agent's instructions to verify it initialized correctly
    print(f"Agent Name: {agent.name}")
    print("✅ Agent initialized successfully.")
    
    # If we had a real key we'd do: agent.print_response("What is Apple's stock price?")
    # Since we don't, we just verify the setup.
except Exception as e:
    print(f"❌ Error during initialization: {e}")
