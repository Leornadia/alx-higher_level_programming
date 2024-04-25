#!/bin/bash
# This script sends a GET request to the provided URL with a custom header X-School-User-Id set to 98 and displays the body of the response.

if [ -z "$1" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

response=$(curl -s -H "X-School-User-Id: 98" "$1")
echo "$response"
