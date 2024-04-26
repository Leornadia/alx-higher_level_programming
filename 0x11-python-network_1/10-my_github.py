#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub
API to display your id.

Usage: ./10-my_github.py <username> <password>
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username, password)

    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print("None")
