#!/usr/bin/python3

"""Defines a square in the python code"""

class Square:
    """Defines a square in the python code
    attributes:
    Size: 1 sided square
    """
    def __init__(self, size=0):
        """Initialises the data inside the class
        args:
        Size: one sided quare
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
