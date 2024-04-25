#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument and displays the body of the response.

if [ -z "$1" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

response=$(curl -s -X DELETE "$1")
echo "$response"
