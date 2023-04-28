#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""

import sys
import requests


def get_github_user_id(username: str, token: str) -> str:
    """
    Retrives the github user id.

    Args:
        username (str): The github username
        token (str): The github personal access token

    Retruns:
        The github user id (str)
        """

    url = "https://api.github.com/user"
    resp = requests.get(url, auth=(username, token))

    if resp.status_code != 200:
        sys.exit("Error: Could not retrieve user id")
    return resp.json().get("id")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: {} username token".format(sys.argv[0]))

    username = sys.argv[1]
    token = sys.argv[2]

    github_user_id = get_github_user_id(username, token)
    print(github_user_id)
