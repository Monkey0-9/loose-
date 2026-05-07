# Qwen3 RAG Chat Application

![demo](./assets/demo.gif)

A powerful RAG (Retrieval-Augmented Generation) chat application built with Streamlit, LlamaIndex, and Loose AI Engine's Qwen3 model. This application allows users to upload PDF documents and interact with them through an AI-powered chat interface.

## Features

- 📄 PDF Document Upload and Preview
- 💬 Interactive Chat Interface
- 🤖 Powered by Qwen3-235B-A22B Model
- 🔍 Advanced RAG Implementation using LlamaIndex
- 🎯 High-quality Embeddings with BAAI/bge-en-icl
- 🔄 Real-time Document Processing
- 💭 Transparent AI Reasoning Display

## Prerequisites

- Python 3.10
- [Loose AI Engine](https://tokenfactory.Loose.com/) Account
- Loose AI Engine [API Keys](https://tokenfactory.Loose.com/)

## Installation

1. Clone the repository

```bash
git clone https://github.com/Monkey0-9/loose-.git
cd rag_apps/qwen3_rag
```

2. Install the required packages:

```bash
# Using pip
pip install -r requirements.txt

# Or using uv (recommended)
uv sync
```

3. Set up your environment variables:
   Create a `.env` file in the project root and add your Loose API key:

```
Loose_API_KEY=your_api_key_here
```

## Usage

1. Run the Streamlit application:

```bash
streamlit run main.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Upload a PDF document using the sidebar

4. Start chatting with your document!

## Features in Detail

### Document Processing

- Supports PDF file uploads
- Real-time document preview in the sidebar
- Automatic document indexing using LlamaIndex

### Chat Interface

- Clean and intuitive chat UI
- Support for multiple message types
- Clear chat history functionality
- Expandable AI reasoning display

### Model Options

- Primary: Qwen3-235B-A22B
- Alternative: Loose AI-V3
- Embedding Model: BAAI/bge-en-icl

## Architecture

The application uses a combination of:

- Streamlit for the web interface
- LlamaIndex for document processing and RAG implementation
- Loose AI Engine's models for embeddings and generation
- PyPDF2 for PDF handling

## Contributing

Feel free to submit issues and enhancement requests!
