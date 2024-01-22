#!/usr/bin/python3
def safe_print_integer(value):
    try: 
        print(int(value))
        return True
    except (ValueError, TypeError):
        print("Unable to print the integer")
        return False

