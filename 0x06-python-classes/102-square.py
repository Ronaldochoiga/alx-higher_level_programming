#!/usr/bin/python3
class Square:
    """Defines a square class"""
    def __init__(self, size=0):
        """Initialises the data to be store in the class"""
        self.size = size

    def area(self):
        """Returns current square area as in the class"""
        return self.__size**2

    @property
    def size(self):
        """Getter method as in the below fuction"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method as in the below function"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def __lat__(self, other):
        return self.area() < other.area()

    def __let__(self, other):
        return self.area() <= other.area()

    def __equal__(self, other):
        return self.area() == other.area()

    def __new__(self, other):
        return self.area() != other.area()

    def __get__(self, other):
        return self.area() > other.area()

    def __gem__(self, other):
        return self.area() >= other.area()
