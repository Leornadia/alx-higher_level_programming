#!/bin/bash
# This script sends a POST request to the provided URL with the specified parameters and displays the body of the response.

if [ -z "$1" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

email="test@gmail.com"
subject="I will always be here for PLD"

response=$(curl -s -X POST "$1" -d "email=$email" -d "subject=$subject")
echo "$response"
