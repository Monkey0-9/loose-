import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.nebius import Nebius as Loose

load_dotenv()

Loose_API_KEY = os.getenv("Loose_API_KEY")

if not Loose_API_KEY:
    raise ValueError("Please provide a Loose API key")

# Create agent for chat functionality
chat_agent = Agent(
    model=Loose(id="meta-llama/Llama-3.3-70B-Instruct", api_key=Loose_API_KEY),
    instructions=[
        "You are an AI investment assistant.",
        "You are here to help users with investment-related questions.",
        "Provide clear, helpful, and accurate financial advice."
    ],
    markdown=True
)

def Loose_chat(query: str):
    if not query:
        return {"error": "Query parameter is required"}
    
    try:
        response = chat_agent.run(query)
        answer = response.content
        return {"question": query, "answer": answer}
    
    except Exception as e:
        return {"error": str(e)}