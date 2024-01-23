#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square.
    
    Attributes:
        __size (int/float): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square.
        Args:
            size (int/float): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2
    
    def __eq__(self, other):
        """Equals to another Square instance by area"""
        return self.area() == other.area()
        
    def __ne__(self, other):
        """Not equal to another Square instance by area"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than another Square instance by area"""
        return self.area() < other.area()
    
    def __le__(self, other):
        """Less than or equal to another Square instance by area"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than another Square instance by area"""
        return self.area() > other.area()
    
    def __ge__(self, other):
        """Greater than or equal to another Square instance by area""" 
        return self.area() >= other.area()
