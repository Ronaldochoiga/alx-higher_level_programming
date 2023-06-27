#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square
    Attributes:
        size: size of a square
    """
    def __init__(self, size=0):
        """Creates new instances
        Args:
            size: size of the square
        """
        self.__size = size

    def area(self):
        """Calculates the area of square.
        Returns: the squareb area
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.
        Args:
            value: size of a square
        Raises:
            TypeError and valueerror
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __lt__(self, other):
        """Rich comparison operator to comp size
        Args:
            other: square to compare size
        Returns: True or false.
        """
        return self.__size < other.__size

    def __le__(self, other):
        """Rich comparison operator to comp size
        Args:
            other: square to compare size
        Returns: True or false.
        """
        return self.__size <= other.__size

    def __eq__(self, other):
        """Rich comparison operator to comp size
        Args:
            other: square to compare size
        Returns: True or false
        """
        return self.__size == other.__size

    def __ne__(self, other):
        """Rich comparison operator to compare area
        Args:
            other: square to compare size.
        Returns: True or false
        """
        return self.__size != other.__size

    def __gt__(self, other):
       """ Compares square area greater
        than another.
        Args:
            other (Square): square to compare size to.
        Returns: True or false
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """Comparison operator to compare square
        Args:
            other: square to compare
        Returns: True or false
        """
        return self.__size >= other.__size
