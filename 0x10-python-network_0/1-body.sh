#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL using curl, and displays the body of the response if the status code is 200.

if [ -z "$1" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

if [ "$response" = "200" ]; then
    body=$(curl -s "$1")
    echo "$body"
fi
