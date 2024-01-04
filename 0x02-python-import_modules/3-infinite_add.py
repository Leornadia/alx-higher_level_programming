#!/usr/bin/env python3
from sys import argv
def infinite_add():
    result = sum(int(arg) for arg in argv[1:])
    print(result)
if __name__ == "__main__":
    infinite_add()
