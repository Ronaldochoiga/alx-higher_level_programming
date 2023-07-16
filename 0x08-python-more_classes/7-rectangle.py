#!/usr/bin/python3
"""Rectangle module.

This module contains a class that defines a rect.

"""


class Rectangle():
    """Defines a rect."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """gives the attributes for the Rect obj.

        Args:
            width (int): the width of the rect.
            height (int): the height of the rect.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """gives the print behavior of the Rect obj."""
        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width + '\n'

        return rectangle[:-1]

    def __repr__(self):
        """gives the repr behavior of the Rect obj."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @property
    def width(self):
        """gives or set the width of the rect."""
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
        """gives or set the height of the rect."""
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
        """gives the rect area."""
        return self.__width * self.__height

    def perimeter(self):
        """gives the rect perim."""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __del__(self):
        """gives the del behavior of the Rect obj."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
