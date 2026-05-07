import asyncio
import os
from agents import (
    Agent,
    OpenAIChatCompletionsModel,
    Runner,
    set_tracing_disabled,
)
from agents.mcp import MCPServerStdio
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

# Constants

EMAIL_MCP_PATH = "/Users/looseai-user/Developer/Python/Loose-Cookbook/Integrations/email-mcp"  
UV_PATH = "/Users/looseai-user/.local/bin/uv"  
MODEL_NAME = "meta-llama/Llama-3.3-70B-Instruct"
API_BASE_URL = "https://api.tokenfactory.Loose.com/v1"
PASSKEY = os.environ["GOOGLE_PASSKEY"]

async def setup_email_agent(mcp_server: MCPServerStdio) -> Agent:
    """Create and configure the Email agent."""
    return Agent(
        name="Email Assistant",
        instructions="""You are an email assistant that helps send emails. 
        First configure the email settings if not done, then help send emails accurately.""",
        mcp_servers=[mcp_server],
        model=OpenAIChatCompletionsModel(
            model=MODEL_NAME,
            openai_client=AsyncOpenAI(
                base_url=API_BASE_URL,
                api_key=os.environ["Loose_API_KEY"]
            )
        )
    )

async def main():
    try:
        async with MCPServerStdio(
            cache_tools_list=True,
            params={
                "command": UV_PATH,
                "args": [
                    "--directory",
                    EMAIL_MCP_PATH,
                    "run",
                    "mcp-server.py"
                ]
            }
        ) as mcp_server:
            email_agent = await setup_email_agent(mcp_server)
            # Integration message - modify as needed
            message = f"""Configure email with sender name 'Loose AI MCP Agent', \
            email 'hello@looseai.dev', and passkey '{PASSKEY}' \
            then send an email to'studioone.tech@gmail.com' with subject \
            'Test Email' and body 'Hello from Email MCP!'"""
            
            try:
                result = await Runner.run(
                    starting_agent=email_agent, 
                    input=message
                )
                print("\nEmail Result:")
                print(result.final_output)
            except Exception as e:
                print(f"\nError with email operation: {e}")
                
    except Exception as e:
        print(f"\nError initializing Email MCP server: {e}")

if __name__ == "__main__":
    set_tracing_disabled(disabled=True)
    asyncio.run(main())
