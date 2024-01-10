#!/usr/bin/python3
from sys import argv
def print_args():
    num_args = len(argv) - 1
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        print(f"1: {argv[1]}")
    else:
        print(f"{num_args} arguments:")
        for i, arg in enumerate(argv[1:], start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    print_args()
