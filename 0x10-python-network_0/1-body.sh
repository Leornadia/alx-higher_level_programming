#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response if the status code is 200

response=$(curl -s -w "%{http_code}" -o /dev/null "$1")
status_code=${response: -3}

if [ $status_code -eq 200 ]; then
    body=$(curl -s "$1")
    echo "$body"
fi
