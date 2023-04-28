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
    commits = resp.json()

    try:
        for i in range(10):
            sha = commits[i]["sha"]
            author_name = commits[i]["commit"]["author"]["name"]
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
