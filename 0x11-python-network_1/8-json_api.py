#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.

Usage: ./8-json_api.py [letter]
"""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {"q": letter}
    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
