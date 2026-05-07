# Base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements or install common libraries directly for speed
RUN pip install --no-cache-dir \
    streamlit \
    rich \
    click \
    python-dotenv \
    agno \
    pydantic \
    pydantic-ai \
    langchain \
    langgraph \
    crewai \
    llamaindex \
    openai \
    google-generativeai \
    requests \
    beautifulsoup4 \
    firecrawl-py \
    qdrant-client

# Copy the entire project
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Command to run the portal by default
CMD ["streamlit", "run", "loose_portal.py"]
