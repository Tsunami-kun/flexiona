#!/bin/bash
# Setup script for Flexiona

# Stop on error
set -e

echo "Setting up Flexiona environment..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not found. Please install Python 3."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Create directories if they don't exist
echo "Setting up directory structure..."
mkdir -p ../static/images
mkdir -p ./chroma_db

# Make scripts executable
chmod +x agent.py
chmod +x utils.py
chmod +x vector_store.py
chmod +x llm_enrichment.py

echo "Setup complete!"
echo "You can now run the agent with: python agent.py"
echo ""
echo "Make sure to set these environment variables before running the agent:"
echo "  - ANTHROPIC_API_KEY - For Claude API access"
echo "  - UNSPLASH_API_KEY - For image suggestions"