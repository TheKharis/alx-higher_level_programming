#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(url)
    print("Body response:")
    print("\t- type: {}" .format(type(resp.text)))
    print("\t- content: {}" .format(resp.text))
