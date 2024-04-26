#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable in the response header.

Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    header_value = response.headers.get("X-Request-Id")

    print(header_value)
