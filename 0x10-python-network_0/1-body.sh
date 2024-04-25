#!/bin/bash
# cURL display body for 200 status code
CODE=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [ "$CODE" = "200" ]; then
    curl -s "$1"
fi
