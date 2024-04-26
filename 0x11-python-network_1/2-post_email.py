#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8).

Usage: ./2-post_email.py <URL> <email>
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("ascii")
    request = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
        print(response_body)
