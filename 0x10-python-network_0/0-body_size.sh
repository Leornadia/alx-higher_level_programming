#!/bin/bash
# This script takes a URL as input, sends a GET request to that URL using curl, and displays the size of the response body in byte 

# Send request to URL
response=$(curl -s $1)

# Get size of response body
size=${#response}

# Print size in bytes
echo $size
