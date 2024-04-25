#!/bin/bash
# cURL display HTTP methods
METHODS=$(curl -s -X OPTIONS -I "$1" | grep "Allow:" | cut -d " " -f2-)
echo "$METHODS"
