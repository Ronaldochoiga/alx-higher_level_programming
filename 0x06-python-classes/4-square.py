#!/usr/bin/python3
class Square:
    """Defines a square as a class"""
    def __init__(self, size=0):
        """Initialises the data contained in the class square"""
        self.size = size

    def area(self):
        """Returns current square area of the class square"""
        return self.__size**2

    @property
    def size(self):
        """Getter method as used above"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method as used in the above function"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
