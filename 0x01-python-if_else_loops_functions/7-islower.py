#!/usr/bin/python3
def islower(c):
    """Checks if c is a lowercase character"""
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
