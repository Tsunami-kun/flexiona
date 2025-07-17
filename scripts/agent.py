#!/usr/bin/env python3
"""
Flexiona Intelligent Agent
--------------------------
This script enhances blog posts with:
1. Automatic article relation via vector similarity
2. Color scheme suggestions based on content
3. Image recommendations
"""

import os
import sys
import glob
import frontmatter
import yaml
import uuid
from typing import List, Dict, Any, Optional
import subprocess

# Import local modules - commented until dependencies are installed
# from vector_store import get_or_create_vector_store
# from llm_enrichment import ContentEnricher
# import utils

# These imports will be used when dependencies are installed
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import SentenceTransformerEmbeddings
# from langchain.text_splitter import MarkdownHeaderTextSplitter
# from langchain_anthropic import AnthropicLLM

# Constants
CONTENT_DIR = "../content/posts"
VECTOR_DB_DIR = "./chroma_db"
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
UNSPLASH_API_KEY = os.environ.get("UNSPLASH_API_KEY", "")


def get_changed_markdown_files() -> List[str]:
    """Get all markdown files that have been modified since the last run.
    
    For initial implementation, we'll just get all markdown files.
    Later this can be optimized to only process changed files using git.
    """
    try:
        # In a git-based workflow, we'd use:
        # return utils.get_git_changed_files(".md")
        # For now, just process all markdown files
        return glob.glob(os.path.join(CONTENT_DIR, "*.md"))
    except Exception as e:
        print(f"Error finding markdown files: {e}")
        return []


def read_markdown_file(file_path: str) -> Dict[Any, str]:
    """Read a markdown file and return its frontmatter and content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            post = frontmatter.load(file)
            return {
                'metadata': post.metadata,
                'content': post.content
            }
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {'metadata': {}, 'content': ''}


def update_front_matter(file_path: str, new_data: Dict[str, Any]) -> bool:
    """Update the frontmatter of a markdown file with new data."""
    try:
        # Read the existing post
        post = frontmatter.load(file_path)
        
        # Update the metadata
        for key, value in new_data.items():
            post[key] = value
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(frontmatter.dumps(post))
        
        return True
    except Exception as e:
        print(f"Error updating frontmatter in {file_path}: {e}")
        return False


def extract_keywords(content: str, num_keywords: int = 5) -> List[str]:
    """Extract main keywords from content.
    
    This is a placeholder. When dependencies are installed, this would use
    LLMs or other NLP techniques to extract keywords.
    """
    # Placeholder implementation
    # In a real implementation, we would use:
    # 1. TF-IDF for a simple approach
    # 2. LLM-based keyword extraction for better results
    return ["academic", "research", "knowledge"]


def update_related_posts(post_filepath: str, vector_store=None) -> None:
    """Find related posts and update the frontmatter."""
    print(f"Processing related posts for {post_filepath}")
    
    # Read the post content
    post_data = read_markdown_file(post_filepath)
    
    # Generate a unique ID for the post based on its filename
    filename = os.path.basename(post_filepath)
    post_id = filename.replace('.md', '')
    
    # When vector_store is available:
    # Add the post to the vector store
    # vector_store.add_document(
    #     document_id=post_id,
    #     text=post_data['content'],
    #     metadata={
    #         'title': post_data['metadata'].get('title', 'Untitled'),
    #         'path': post_filepath,
    #         'url': f"/posts/{post_id}/"
    #     }
    # )
    # 
    # # Find related posts
    # similar_docs = vector_store.similarity_search(post_data['content'], k=5)
    # 
    # # Filter out the current post
    # related_posts = []
    # for doc in similar_docs:
    #     if doc['id'] != post_id:
    #         related_posts.append({
    #             'title': doc['metadata']['title'],
    #             'url': doc['metadata']['url']
    #         })
    
    # Placeholder for now
    related_posts = [
        {'title': 'Sample Related Post 1', 'url': '/posts/sample1/'},
        {'title': 'Sample Related Post 2', 'url': '/posts/sample2/'}
    ]
    
    # Update the frontmatter
    update_front_matter(post_filepath, {'related_posts': related_posts})


def suggest_color_scheme(post_filepath: str, enricher=None) -> None:
    """Generate a color scheme suggestion based on the post content."""
    print(f"Suggesting colors for {post_filepath}")
    
    # Read the post content
    post_data = read_markdown_file(post_filepath)
    title = post_data['metadata'].get('title', 'Untitled')
    
    # When enricher is available:
    # colors = enricher.generate_color_scheme(title, post_data['content'][:1000])
    
    # Placeholder for now
    colors = ['#2c3e50', '#e74c3c', '#ecf0f1', '#3498db', '#2ecc71']
    
    # Update the frontmatter
    update_front_matter(post_filepath, {'colors': colors})


def suggest_image(post_filepath: str, enricher=None) -> None:
    """Suggest a relevant image for the post."""
    print(f"Suggesting image for {post_filepath}")
    
    # Skip if no Unsplash API key
    if not UNSPLASH_API_KEY:
        print("Skipping image suggestion - no Unsplash API key provided")
    
    # Read the post content
    post_data = read_markdown_file(post_filepath)
    
    # When utils and enricher are available:
    # # Extract keywords
    # keywords = enricher.extract_keywords(post_data['content'])
    # # Search Unsplash for images
    # image_data = utils.search_unsplash(keywords, UNSPLASH_API_KEY)
    # if image_data:
    #     update_front_matter(post_filepath, {'suggested_image': image_data})
    
    # Placeholder for now
    update_front_matter(post_filepath, {
        'suggested_image': {
            'url': 'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8',
            'alt': 'Academic research image',
            'credit': {
                'name': 'Unsplash Photographer',
                'link': 'https://unsplash.com'
            }
        }
    })


def generate_article_summary(post_filepath: str, enricher=None) -> None:
    """Generate a summary for the article."""
    print(f"Generating summary for {post_filepath}")
    
    # Read the post content
    post_data = read_markdown_file(post_filepath)
    
    # When enricher is available:
    # summary = enricher.generate_summary(post_data['content'])
    
    # Placeholder summary
    summary = "This is an automatically generated summary of the article."
    
    # Update the frontmatter
    update_front_matter(post_filepath, {'summary': summary})


def main() -> None:
    """Main execution function."""
    # Check if we're in the right directory
    if not os.path.exists(CONTENT_DIR):
        # Try to adjust path if script is run from Hugo root
        global CONTENT_DIR
        CONTENT_DIR = "./content/posts"
        if not os.path.exists(CONTENT_DIR):
            print(f"Error: Cannot find content directory at {CONTENT_DIR}")
            sys.exit(1)
    
    print("Flexiona Intelligent Agent starting...")
    
    # Initialize vector store - commented until dependencies are installed
    # vector_store = get_or_create_vector_store(VECTOR_DB_DIR)
    
    # Initialize content enricher - commented until dependencies are installed
    # enricher = ContentEnricher(ANTHROPIC_API_KEY)
    
    # Get all markdown files that need processing
    md_files = get_changed_markdown_files()
    print(f"Found {len(md_files)} markdown files to process")
    
    # Process each file
    for file_path in md_files:
        print(f"\nProcessing: {file_path}")
        update_related_posts(file_path)  # vector_store
        suggest_color_scheme(file_path)  # enricher
        suggest_image(file_path)  # enricher
        generate_article_summary(file_path)  # enricher
    
    print("\nProcessing complete!")


if __name__ == "__main__":
    main()