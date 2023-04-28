#!/usr/bin/python3
"""
A Python script that takes 2 arguments in order list 10 commits (from the most
recent to oldest) of the repository “rails” by the user “rails”
"""

import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    resp = requests.get(url)

    if resp.status_code == 200:
        commits = resp.json()
        for commit in commits:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
    else:

        print(f"Error retrieving commits: {resp.status_code}")
