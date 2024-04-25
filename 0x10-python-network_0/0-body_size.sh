#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Send a request to the URL and store the response in a variable
response=$(curl -sI "$url")

# Extract the content length from the response headers
content_length=$(echo "$response" | grep -i 'content-length' | awk '{print $2}')

# Display the content length (size) in bytes
echo "Content length (bytes): $content_length"

