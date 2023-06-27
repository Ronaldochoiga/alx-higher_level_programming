#!/usr/bin/python3

"""Defines the square in question"""

class Square:
   """
    Class that defines properties of square by:
    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size): 
       """Creates new instances of square (1 side).
        Args:
            size: size of the square.
        """
       self.__size = size
