#!/usr/bin/python3
"""
Lists the 10 most recent commits of a given GitHub repository.

Usage: ./100-github_commits.py <repository> <owner>
"""
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit.get("sha")
            author_name = commit.get("commit", {}).get("author", {}).get("name")
            print(f"{sha}: {author_name}")
    else:
        print("Failed to retrieve commits.")
