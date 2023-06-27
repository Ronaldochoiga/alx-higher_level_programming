#!/usr/bin/python3
"""Defines a square class"""

class Square:
    """
    Anitializes the function
    Attribute:
    Size: size of the square
    """
    def __init__(self, size=0):
        """creates new instance
        Args:
        Size: size of the square
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns current square area held by size
        """
        return self.__size**2
