# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Flexiona (流域) is a modern, intelligent academic blog platform that combines Hugo's static site generation with AI-powered content enhancement. The core philosophy is "content and intelligence separation, Git as a database" where authors focus on writing Markdown content while intelligent processing happens through automated scripts.

## Key Commands

### Development

```bash
# Start Hugo development server with drafts enabled
hugo server -D

# Create a new blog post
hugo new content posts/your-post-name.md
```

### Agent Operations

```bash
# Install Python dependencies for the intelligent agent
cd scripts
./setup.sh
cd ..

# Run the intelligent agent manually to process all posts
cd scripts
python agent.py
cd ..
```

### Deployment

```bash
# Build the site for production
hugo --minify
```

## Environment Variables

The intelligent agent requires these environment variables:

- `ANTHROPIC_API_KEY` - For Claude API access (content enhancement)
- `UNSPLASH_API_KEY` - For automatic image suggestions

## Architecture

The project is divided into two main components:

1. **Hugo Site (Frontend)**
   - Uses the PaperMod theme with LaTeX support
   - Content stored in `content/posts/` as Markdown files
   - Configuration in `config.toml`

2. **Intelligent Agent (Python)**
   - Located in the `scripts/` directory
   - Enhances blog content through AI-powered analysis
   - Core modules:
     - `agent.py`: Main entry point that processes blog posts
     - `vector_store.py`: Handles document embedding and similarity search
     - `llm_enrichment.py`: Manages LLM-based content enhancement
     - `utils.py`: Contains utility functions for file operations and API calls

### Data Flow

1. Authors create content as Markdown files with frontmatter
2. The intelligent agent processes each Markdown file to:
   - Add related posts via vector similarity search
   - Generate color scheme suggestions
   - Recommend relevant images
   - Create automatic summaries
3. Enhanced metadata is written to each post's frontmatter
4. Hugo builds the final site using this enhanced metadata

### Dependency Stack

- **Hugo**: Static site generator with PaperMod theme
- **Python 3**: Powers the intelligent agent
- **LangChain**: Framework for LLM applications
- **ChromaDB**: Vector database for similarity search
- **Sentence-Transformers**: Embedding models for text vectorization
- **Claude API**: For high-quality content enhancement
- **Unsplash API**: For automatic image suggestions

## Important Implementation Details

- The agent is designed to run during the build process on Vercel/Netlify
- Local implementation uses placeholders for some functionality until dependencies are installed
- Vector database is stored locally in `scripts/chroma_db/`
- The agent automatically adapts paths whether run from Hugo root or scripts directory