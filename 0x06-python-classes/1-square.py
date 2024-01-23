#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size if isinstance(size, int) else 0
