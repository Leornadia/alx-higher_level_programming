#!/usr/bin/python3
"""Function to read UTF8 text file and print to stdout"""

def read_file(filename=""):
    """Read filename and print to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
