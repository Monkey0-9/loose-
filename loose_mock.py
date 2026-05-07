import os
from unittest.mock import MagicMock

def initialize_sandbox():
    """
    Initialize the simulation environment for autonomous modules.
    Ensures safe execution across all integrated frameworks.
    """
    os.environ["USE_MOCK"] = "1"
    os.environ["LOOSE_API_KEY"] = "mock-loose-key-2026"
    os.environ["OPENAI_API_KEY"] = "sk-mock-key"
    
    print("[Loose AI] Initializing Simulation Environment...")
    
    # 1. Intelligence Core Simulation
    try:
        from openai import OpenAI
        OpenAI.chat = MagicMock()
        print("   -> Intelligence Core: [INITIALIZED]")
    except ImportError:
        pass

    # 2. Logic Orchestration Simulation
    try:
        import agno
        import agno.agent
        agno.agent.Agent = MagicMock()
        print("   -> Logic Orchestration: [INITIALIZED]")
    except ImportError:
        pass

    # 3. Financial Intelligence Simulation
    try:
        import yfinance
        yfinance.Ticker = MagicMock()
        print("   -> Financial Pipeline: [INITIALIZED]")
    except ImportError:
        pass

    # 4. Search Ecosystem Simulation
    try:
        import duckduckgo_search
        duckduckgo_search.DDGS = MagicMock()
        print("   -> Knowledge Retrieval: [INITIALIZED]")
    except ImportError:
        pass

    # 5. Strands Framework Simulation
    try:
        import strands
        import strands_tools

        class CustomStrandsEngine:
            def __init__(self, **kwargs):
                self.name = kwargs.get("name", "StrandsModule")

            def __call__(self, query):
                print(f"\n[Strands Module: {self.name}] Processing: {query}")
                return f"[Loose AI] Simulation response for: {query}"

        strands.Agent = CustomStrandsEngine
        strands.models.litellm.LiteLLMModel = MagicMock()
        strands_tools.http_request = MagicMock()
        print("   -> Strands Integration: [INITIALIZED]")
    except ImportError:
        pass

    print("[Loose AI] Simulation Environment Ready.\n")


if __name__ == "__main__":
    initialize_sandbox()
