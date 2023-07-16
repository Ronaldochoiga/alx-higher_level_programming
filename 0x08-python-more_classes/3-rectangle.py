#!/usr/bin/python3
"""Rect module.

This module contains a class that defines a rect.

"""


class Rectangle():
    """Defines a rect."""

    def __init__(self, width=0, height=0):
        """Sets the necessary attributes for the rect obj.

        Args:
            width (int): the width of the rect.
            height (int): the height of the rect.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Sets the print behavior of the rect obj."""
        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += '#' * self.__width + '\n'

        return rectangle[:-1]

    @property
    def width(self):
        """Gets the width of the rect."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """sets the height of the rect."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Returns the current rect area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the current rect perim."""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2
