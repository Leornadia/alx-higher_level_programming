#!/usr/bin/env python3
import importlib
import sys

if sys.version_info < (3, 8):
    print("This script requires Python 3.8+")
    exit(1)

hidden_module = importlib.import_module("hidden_4")
names = dir(hidden_module)

for name in sorted(names):
    if not name.startswith("__"):
        print(name)
