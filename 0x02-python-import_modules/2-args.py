#!/usr/bin/env python3
import sys

def print_args():
    argc = len(sys.argv) - 1  
    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, "s"[argc==1:]))
    
    if argc > 0:
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
            
if __name__ == "__main__":
    print_args()
