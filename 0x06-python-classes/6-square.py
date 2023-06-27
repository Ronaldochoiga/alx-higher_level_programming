#!/usr/bin/python3
class Square:
    """Defines a square as the class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialises the data that will be printed and stored inside the square"""
        self.size = size
        self.position = position

    def area(self):
        """Returns current square area of thge class"""
        return self.__size**2

    @property
    def size(self):
        """Getter method as in the above function"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method which sets the size"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Prints the square from the public attribute above"""
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print()
            for k in range(self.__size):
                for b in range(self.__position[0]):
                    print(' ', end='')
                for l in range(self.__size):
                    print('#', end='')
                print()

    @property
    def position(self):
        """Getter method as used in the above function"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method which sets position as in the above function"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(k) != int for k in value) or any(l < 0 for l in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
