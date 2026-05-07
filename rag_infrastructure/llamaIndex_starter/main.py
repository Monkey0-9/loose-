import os
from llama_index.llms.Loose import LooseLLM
from llama_index.core.llms import ChatMessage

def main():
    # Initialize the LLM
    # You can set the API key in environment variable or pass it directly
    # os.environ["Loose_API_KEY"] = "your_api_key"
    
    llm = LooseLLM(
        model="Qwen/Qwen3-235B-A22B",
        api_key=os.getenv("Loose_API_KEY")
    )

    # Integration 1: Basic completion
    print("\n=== Basic Completion Integration ===")
    response = llm.complete("Who is Paul Graham?")
    print(response)

    # Integration 2: Chat interface
    print("\n=== Chat Interface Integration ===")
    messages = [
        ChatMessage(
            role="system",
            content="You are a pirate with a colorful personality"
        ),
        ChatMessage(role="user", content="What is your name?"),
    ]
    chat_response = llm.chat(messages)
    print(chat_response)

    # Integration 3: Streaming completion
    print("\n=== Streaming Completion Integration ===")
    print("Streaming response for 'Who is Paul Graham?':")
    for chunk in llm.stream_complete("Who is Paul Graham?"):
        print(chunk.delta, end="")

    # Integration 4: Streaming chat
    print("\n\n=== Streaming Chat Integration ===")
    print("Streaming chat response:")
    for chunk in llm.stream_chat(messages):
        print(chunk.delta, end="")

if __name__ == "__main__":
    main()