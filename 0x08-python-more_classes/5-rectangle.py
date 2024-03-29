#!/usr/bin/python3

"""Rectangle Class.

This module contains an class that defines a rect.

Usage Example:

    Rectangle = __import__('0-rectangle').Rectangle

    my_rectangle = Rectangle()
    print(type(my_rectangle))
    print(my_rectangle.__dict__)
"""


class Rectangle:
    """Defines the sides of a rectangle.

    Attribute:
        width: An integer showing the width of the rect obj.
        height: An integer showing the height of the rect obj.
    """

    def __init__(self, width=0, height=0):
        """An object construt method.

        assigns Rect with width and height.

        Args:
            width: An integer showing object width.
                  default is value of 0.
            height: An integer showing object height.
                  default is value of 0.
        """
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a printable string representation
        of a Rectangle for instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += "#"
            rec_str += "\n"
        return rec_str[:-1]

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to create a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Print a message for del
        """
        print("Bye rectangle...")

    @property
    def width(self):
        """Gets the width private att value.

        Returns:
            The width private att
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width att value.

        Validates the assignment of the width att.

        Arg:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height priv att value.

        Returns:
            The height priv att
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height priv att value.

        Validates the assignment of the height priv att.

        Arg:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A public object method.

        Returns:
            The current rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """A public object method.

        Returns:
            The current rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
