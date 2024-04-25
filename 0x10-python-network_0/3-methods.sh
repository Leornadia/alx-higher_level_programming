#!/bin/bash
# This script takes a URL as an argument and displays all HTTP methods the server will accept.

if [ -z "$1" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

methods=$(curl -s -X OPTIONS -I "$1" | grep "Allow:" | cut -d " " -f2-)
echo "$methods"
