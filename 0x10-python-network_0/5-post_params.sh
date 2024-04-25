#!/bin/bash
# cURL send POST request with parameters
EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"
curl -s -X POST "$1" -d "email=$EMAIL" -d "subject=$SUBJECT"
