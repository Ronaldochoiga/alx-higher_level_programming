#!/usr/bin/python3
"""Rectangle module.

This module contains a class that defines a rectangle.

"""


class Rectangle():
    """Defines a rect."""

    def __init__(self, width=0, height=0):
        """Sets or gets the attributes for the rect object.

        Args:
            width (int): the width of the rect.
            height (int): the height of the rect.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """sets the width of the rect."""
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
        """Gets the height of the rect."""
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
        """gives the current rect area."""
        return self.__width * self.__height

    def perimeter(self):
        """gives the current rect perim."""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2
