#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square
    Attributes:
        size: size of a square
    """
    def __init__(self, size=0):
        """Creates new instance
        Args:
            size: size of the square
        """
        self.__size = size

    def area(self):
        """Calculates the area of square.
        Returns: the area
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
            value error and type error
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout
        """

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * (self.__size))
