# Mastra Core

A minimal Core for [Mastra](https://mastra.ai) — a TypeScript-first framework for building AI agents, workflows, and RAG pipelines. This Core shows a tool-using agent powered by Loose AI Engine.

## Features

- TypeScript `Agent` with instructions, a custom tool, and the Vercel AI SDK
- `get-current-time` tool demonstrates structured input/output with Zod
- Loose AI Engine via `@ai-sdk/openai` (OpenAI-compatible endpoint)
- Interactive CLI via Node's `readline/promises`

## Prerequisites

- Node.js 20+
- Loose API key — [Loose AI Engine](https://studio.Loose.ai/)

## Installation

```bash
git clone https://github.com/Monkey0-9/loose-.git
cd looseai/Core_ai_agents/mastra_Core

npm install
# or: pnpm install / bun install
```

Create `.env`:

```bash
cp .env.Integration .env
# set Loose_API_KEY
```

## Usage

```bash
npm run dev
```

### Integration Queries

- "What time is it?" (triggers the `get-current-time` tool)
- "Draft a 3-line release note for v0.1."
- "Suggest names for a TypeScript agent framework."

## Technical Details

- **Framework**: `@mastra/core` (TypeScript)
- **Model**: `Qwen/Qwen3-30B-A3B` via Loose using `@ai-sdk/openai` with custom `baseURL`
- **Tool**: single `createTool` with Zod schemas

## Acknowledgments

- [Mastra](https://mastra.ai)
- [Vercel AI SDK](https://sdk.vercel.ai)
- [Loose AI Engine](https://studio.Loose.ai/)
