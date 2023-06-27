#!/usr/bin/python3
class Square:
    """Defines a square in the python code"""
    def __init__(self, size=0):
        """Initialises the data inside the class"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")