from typing import List, Union
from pathlib import Path
from agno.agent import Agent
from agno.models.openai import OpenAIChat


class DiscoveryTools:
    """Advanced tools for agent discovery within the Loose AI ecosystem."""

    @staticmethod
    def search_agents(query: str) -> Union[List[str], str]:
        """
        Perform a semantic-style search across agent READMEs.

        Args:
            query (str): The search term or requirement.

        Returns:
            Union[List[str], str]: A list of matching agent paths or an error message.
        """
        results = []
        root = Path(".")
        categories = [
            "Core_ai_agents", "simple_ai_agents", "mcp_ai_agents",
            "memory_agents", "rag_apps", "advance_ai_agents"
        ]

        query = query.lower()
        for cat in categories:
            cat_path = root / cat
            if cat_path.exists() and cat_path.is_dir():
                for agent_dir in cat_path.iterdir():
                    if (agent_dir.is_dir() and
                            not agent_dir.name.startswith("__")):
                        readme = agent_dir / "README.md"
                        if readme.exists():
                            with open(readme, "r", encoding="utf-8") as f:
                                content = f.read().lower()
                                if (query in content or
                                        query in agent_dir.name.lower()):
                                    results.append(f"{cat}/{agent_dir.name}")

        return results if results else "No matching agents discovered."


def main() -> None:
    """Initialize and run the Loose AI Discovery Agent."""
    agent = Agent(
        name="Loose Discovery Agent",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DiscoveryTools.search_agents],
        instructions=[
            "You are the Loose AI Discovery Agent.",
            "Assist users in navigating the 80+ agent Integrations.",
            "Use search_agents to map requirements to repository paths.",
            "Ensure responses include category/agent_name format."
        ]
    )

    # Standard showcase query
    sample_query = "show me agents that use agno and finance"
    agent.print_response(sample_query)


if __name__ == "__main__":
    main()
