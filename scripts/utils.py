#!/usr/bin/env python3
"""
Utility functions for the Flexiona Intelligent Agent
"""

import os
import subprocess
from typing import List, Dict, Any, Optional
import requests
import json


def run_git_command(command: List[str]) -> str:
    """Run a git command and return the output."""
    try:
        result = subprocess.run(
            ["git"] + command,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Git command error: {e}")
        return ""


def get_git_changed_files(file_extension: str = ".md") -> List[str]:
    """Get files changed since last commit with the specified extension."""
    try:
        # Get files that have been modified but not staged
        unstaged = run_git_command(["diff", "--name-only"])
        # Get files that have been staged
        staged = run_git_command(["diff", "--cached", "--name-only"])
        # Get untracked files
        untracked = run_git_command(["ls-files", "--others", "--exclude-standard"])
        
        # Combine all files and filter by extension
        all_files = unstaged.split("\n") + staged.split("\n") + untracked.split("\n")
        return [f for f in all_files if f.endswith(file_extension)]
    except Exception as e:
        print(f"Error getting changed files: {e}")
        return []


def search_unsplash(keywords: List[str], api_key: str) -> Optional[Dict[str, Any]]:
    """Search Unsplash for images based on keywords."""
    if not api_key:
        print("Unsplash API key not provided")
        return None
    
    query = " ".join(keywords)
    url = f"https://api.unsplash.com/search/photos"
    
    headers = {
        "Authorization": f"Client-ID {api_key}"
    }
    
    params = {
        "query": query,
        "per_page": 1,
        "orientation": "landscape"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data["results"]:
            return {
                "url": data["results"][0]["urls"]["regular"],
                "alt": data["results"][0]["alt_description"] or "Image related to " + query,
                "credit": {
                    "name": data["results"][0]["user"]["name"],
                    "link": data["results"][0]["user"]["links"]["html"]
                }
            }
        return None
    except Exception as e:
        print(f"Error searching Unsplash: {e}")
        return None