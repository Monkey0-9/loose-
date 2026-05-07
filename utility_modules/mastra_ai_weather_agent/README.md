# Using a tool with Mastra AI and Loose 

A simple Integration showing how to use a tool.

## Prerequisites

- Node.js v20.0+
- pnpm (recommended) or npm
- Loose AI Engine Key

## Getting Started

1. Copy the environment variables file and add your OpenAI API key:

   ```bash
   cp .env.Integration .env
   ```

   Then edit `.env` and add your OpenAI API key:

   ```env
   Loose_API_KEY=your-api-key-here
   ```

2. Install dependencies:

   ```
   pnpm install
   ```

3. Run the Integration:

   ```bash
   pnpm start
   ```
