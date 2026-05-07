"""
Loose AI — Gossip Agent (Memory Agent)
A CLI agent that remembers facts across sessions via a JSON file store.
PydanticAI-inspired typed state management.

Run:  python main.py
"""

import os
import sys
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

MEMORY_FILE = Path(__file__).parent / "memory.json"


# ─────────────────────────────────────────────────────────────────
# Typed Memory State (PydanticAI style)
# ─────────────────────────────────────────────────────────────────
class MemoryState(BaseModel):
    """Persistent agent memory across sessions."""
    user_name:    str       = Field(default="", description="Remembered user name")
    topics_seen:  list[str] = Field(default_factory=list)
    facts:        dict[str, str] = Field(default_factory=dict)
    turn_count:   int       = 0
    last_seen:    str       = ""

    def save(self, path: Path = MEMORY_FILE):
        path.write_text(self.model_dump_json(indent=2))

    @classmethod
    def load(cls, path: Path = MEMORY_FILE) -> "MemoryState":
        if path.exists():
            try:
                return cls.model_validate_json(path.read_text())
            except Exception:
                pass  # Corrupt file → fresh state
        return cls()

    def record_turn(self, user_input: str):
        """Update state based on the user's latest message."""
        self.turn_count += 1
        self.last_seen = datetime.now().isoformat()

        # Extract name if user introduces themselves
        name_match = re.search(r"\bmy name is ([A-Za-z]+)", user_input, re.I)
        if name_match:
            self.user_name = name_match.group(1).capitalize()

        # Record topic keywords
        words = [w.lower() for w in re.findall(r"[a-zA-Z]{4,}", user_input)]
        stop = {"that", "this", "what", "with", "from", "have", "about", "tell", "your", "know"}
        topics = [w for w in words if w not in stop][:3]
        self.topics_seen = list(dict.fromkeys(self.topics_seen + topics))[-20:]  # keep last 20

        # Extract simple "X is Y" facts
        fact_match = re.search(r"([A-Za-z ]+) is ([A-Za-z ]+)", user_input)
        if fact_match:
            key, val = fact_match.group(1).strip().lower(), fact_match.group(2).strip()
            self.facts[key] = val


# ─────────────────────────────────────────────────────────────────
# Mock LLM with memory injection
# ─────────────────────────────────────────────────────────────────
def mock_response(user_input: str, state: MemoryState) -> str:
    name_part    = f"Hi {state.user_name}! " if state.user_name else ""
    topic_part   = f"We've talked about: {', '.join(state.topics_seen[-3:])}. " if state.topics_seen else ""
    fact_part    = ""
    if state.facts:
        fact_str  = "; ".join(f"{k}={v}" for k, v in list(state.facts.items())[-2:])
        fact_part = f"I remember: {fact_str}. "

    return (
        f"{name_part}[Mock Reply | Turn {state.turn_count}] "
        f"{topic_part}{fact_part}"
        f"You said: '{user_input[:60]}'. (Set USE_REAL_LLM=1 for AI responses.)"
    )


def real_response(user_input: str, state: MemoryState, history: list[dict], api_key: str) -> str:
    import openai
    client = openai.OpenAI(api_key=api_key)
    memory_context = ""
    if state.user_name:
        memory_context += f"The user's name is {state.user_name}. "
    if state.facts:
        memory_context += "Known facts: " + "; ".join(f"{k}={v}" for k, v in state.facts.items()) + ". "
    if state.topics_seen:
        memory_context += f"Past topics: {', '.join(state.topics_seen[-5:])}. "

    system = (
        "You are a friendly assistant with a good memory. "
        f"Persistent memory context: {memory_context or 'None yet.'}"
    )
    messages = [{"role": "system", "content": system}] + history
    messages.append({"role": "user", "content": user_input})
    resp = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return resp.choices[0].message.content


# ─────────────────────────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────────────────────────
def main():
    api_key  = os.getenv("OPENAI_API_KEY", "")
    use_real = os.getenv("USE_REAL_LLM") == "1"

    if use_real and not api_key:
        print("ERROR: OPENAI_API_KEY required when USE_REAL_LLM=1", file=sys.stderr)
        sys.exit(1)

    state   = MemoryState.load()
    history: list[dict] = []

    greeting = f"\n🧠 Loose AI — Gossip Agent [{'Real' if use_real else 'Mock'}]"
    if state.user_name:
        greeting += f"\nWelcome back, {state.user_name}! (Turn #{state.turn_count + 1})"
    else:
        greeting += "\nI remember things you tell me across sessions."
    print(greeting)
    print("Type 'memory' to see what I know. Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSaving memory… Goodbye!")
            state.save()
            break

        if user_input.lower() in {"exit", "quit"}:
            state.save()
            print("Memory saved. Goodbye!")
            break

        if user_input.lower() == "memory":
            print(f"\n📝 Memory snapshot:\n{state.model_dump_json(indent=2)}\n")
            continue

        if not user_input:
            continue

        state.record_turn(user_input)

        try:
            if use_real:
                reply = real_response(user_input, state, history, api_key)
            else:
                reply = mock_response(user_input, state)
        except Exception as e:
            reply = f"⚠️ Error: {e}"

        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": reply})
        print(f"\nAgent: {reply}\n")
        state.save()


if __name__ == "__main__":
    main()
