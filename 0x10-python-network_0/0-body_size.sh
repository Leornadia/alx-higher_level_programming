#!/bin/bash
# This script sends a request to a URL and displays the size of the response body in bytes

response=$(curl -s "$1") # Send a silent request to the URL and store the response
size=${#response} # Get the length of the response string
echo "$size" # Print the size of the response body
