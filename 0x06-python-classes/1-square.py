#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square.
    """
    
    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square.
        """
        assert isinstance(size, int), "size must be an integer"
        assert size >= 0, "size must be >= 0"
        self.__size = size

