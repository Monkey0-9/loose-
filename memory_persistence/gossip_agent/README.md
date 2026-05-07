# Gossip Agent — Loose AI (Memory Agent)

A CLI agent that **remembers conversations** across sessions using a JSON file store.

## Features
- Persistent memory: recalls names, preferences, past topics
- PydanticAI-style typed state
- Works entirely without real API keys

## Setup

```bash
pip install -r requirements.txt
cp .env.Integration .env
python main.py
```

## Notes
- Memory is stored in `memory.json` in the same directory
- Delete `memory.json` to reset
