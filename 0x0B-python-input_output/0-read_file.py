#!/usr/bin/python3

"""
Module Description:
This module contains a function to read a text file and print its contents to stdout.

Function(s):
- read_file(filename=""): Reads the content of the specified text file and prints it to stdout.

Example Usage:
>>> read_file("example.txt")
This is the content of example.txt.
"""

def read_file(filename=""):
    """
    Function Description:
    Reads the content of the specified text file and prints it to stdout.

    Parameters:
    - filename (str): The name of the text file to be read. Defaults to an empty string.

    Returns:
    None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
