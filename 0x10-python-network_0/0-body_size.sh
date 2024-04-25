#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL using curl, and displays the size of the response body in bytes.

if [ -z "$1" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

response=$(curl -s "$1")
size=${#response}

echo "$size"
