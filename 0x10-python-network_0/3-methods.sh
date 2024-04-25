#!/bin/bash
# cURL display HTTP method 
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
