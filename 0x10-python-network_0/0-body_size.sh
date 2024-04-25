#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

url=$1
body_size=$(curl -s -w "%{size_download}\n" -o /dev/null $url)
echo $body_size

