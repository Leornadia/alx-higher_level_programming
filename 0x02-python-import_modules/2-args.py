#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args_len = len(sys.argv) - 1
    args_plural = "arguments" if args_len != 1 else "argument"
    print("{} {}{}{}".format(args_len, args_plural, ":" if args_len else ".", "" if args_len == 0 else "\n"))
    for i, arg in enumerate(sys.argv[1:], 1):
        print("{}: {}".format(i, arg))
