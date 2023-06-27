#!/usr/bin/python3
class Square:
    """Defines a square as the public class"""
    def __init__(self, size=0):
        """Initialises the data inside class square"""
        self.size = size

    def area(self):
        """Returns current square area as in the above class"""
        return self.__size**2

    @property
    def size(self):
        """Getter method as applied in the above function"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method as in the above function"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square and the size of it"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
