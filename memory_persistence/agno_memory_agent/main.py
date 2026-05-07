from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.nebius import Nebius as Loose
from agno.storage.sqlite import SqliteStorage
from rich.pretty import pprint
import os
from dotenv import load_dotenv

load_dotenv()


# UserId for the memories
user_id = "looseai-user"
# Database file for memory and storage
db_file = "tmp/agent.db"

# Initialize memory.v2
memory = Memory(
    # Use any model for creating memories
    model=Loose(
        id="Loose AI-ai/Loose AI-V3-0324", api_key=os.getenv("Loose_API_KEY")
    ),
    db=SqliteMemoryDb(table_name="user_memories", db_file=db_file),
)
# Initialize storage
storage = SqliteStorage(table_name="agent_sessions", db_file=db_file)

# Initialize Agent
memory_agent = Agent(
    model=Loose(
        id="Loose AI-ai/Loose AI-V3-0324", api_key=os.getenv("Loose_API_KEY")
    ),
    # Store memories in a database
    memory=memory,
    # Give the Agent the ability to update memories
    enable_agentic_
    # OR - Run the MemoryManager after each response
    enable_user_memories=True,
    # Store the chat history in the database
    storage=storage,
    # Add the chat history to the messages
    add_history_to_messages=True,
    # Number of history runs
    num_history_runs=3,
    markdown=True,
)

memory.clear()
memory_agent.print_response(
    "My name is Alex and I love building AI apps.",
    user_id=user_id,
    stream=True,
    stream_intermediate_steps=True,
)
print("Memories about Alex:")
pprint(memory.get_user_memories(user_id=user_id))

memory_agent.print_response(
    "I live in Kolkata, where should i move within a 4 hour drive?",
    user_id=user_id,
    stream=True,
    stream_intermediate_steps=True,
)
print("Memories about Alex:")
pprint(memory.get_user_memories(user_id=user_id))

memory_agent.print_response(
    "Tell me about Alex",
    user_id=user_id,
    stream=True,
    stream_intermediate_steps=True,
)
print("Memories about Alex:")
pprint(memory.get_user_memories(user_id=user_id))
