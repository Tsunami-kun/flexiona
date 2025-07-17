# Flexiona (流域) - Intelligent Academic Blog Platform

Flexiona is a modern, intelligent academic blog platform that combines Hugo's speed with AI-powered content enhancement.

## Core Philosophy

**"Content and intelligence separation, Git as a database"**

Authors focus on writing quality Markdown content, while intelligent processing happens through automated scripts.

## Features

- **Academic Focus**: Built for research presentation with LaTeX support
- **Intelligent Linking**: Automatically connects related posts via content similarity
- **Aesthetic Enhancement**: Suggests color schemes based on content
- **Visual Support**: Recommends relevant images for articles
- **Version Controlled**: All content stored in Git for easy tracking and collaboration

## Technology Stack

- **Content Core**: Git + Markdown
- **Frontend Framework**: Hugo with PaperMod theme
- **Intelligence Hub**: Python + LangChain
- **Data/Models**: 
  - ChromaDB (local vector database)
  - Sentence-Transformers (lightweight embedding models)
  - Claude API (for high-quality summaries and enhancements)
  - Unsplash API (for automatic image suggestions)
- **Deployment**: Vercel or Netlify

## Getting Started

### Local Development

1. **Install Hugo**
   
   Follow the [official Hugo installation guide](https://gohugo.io/installation/).

2. **Clone this repository**

   ```bash
   git clone https://github.com/yourusername/flexiona.git
   cd flexiona
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory:

   ```
   ANTHROPIC_API_KEY=your_claude_api_key
   UNSPLASH_API_KEY=your_unsplash_api_key
   ```

4. **Install dependencies**

   ```bash
   cd scripts
   ./setup.sh
   cd ..
   ```

5. **Start the development server**

   ```bash
   hugo server -D
   ```

6. **Create new content**

   ```bash
   hugo new content posts/my-new-post.md
   ```

7. **Run the intelligent agent**

   ```bash
   cd scripts
   python agent.py
   cd ..
   ```

### Deployment

The project is configured for easy deployment on Vercel:

1. Connect your GitHub repository to Vercel
2. Set the required environment variables in the Vercel project settings
3. Deploy!

## Workflow

1. Write Markdown content locally in the `content/posts` directory
2. Add images to `static/images` if needed
3. Commit and push to GitHub
4. The intelligent agent runs automatically during deployment
5. The agent enhances your content with:
   - Related article links
   - Color scheme suggestions
   - Image recommendations
   - Automatic summaries
6. Hugo builds the final site with these enhancements
7. The site is deployed to Vercel's global CDN

## License

[MIT License](LICENSE)

## Acknowledgments

- This project uses the [Hugo PaperMod theme](https://github.com/adityatelange/hugo-PaperMod)
- Powered by [LangChain](https://github.com/langchain-ai/langchain) for AI components