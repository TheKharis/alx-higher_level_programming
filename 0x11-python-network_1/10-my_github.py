#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: {} username token".format(sys.argv[0]))

    url = "https://api.github.com/user"
    username = sys.argv[1]
    token = sys.argv[2]

    resp = requests.get(url, auth=(username, token))

    if resp.status_code != 200:
        sys.exit("Error: Could not retrieve user id")

    print(resp.json().get("id"))
