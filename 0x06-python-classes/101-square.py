#!/usr/bin/python3
class Square:
    """Defines a square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialises the data from the class"""
        self.size = size
        self.position = position

    def area(self):
        """Returns current square area of the square class"""
        return self.__size**2

    @property
    def size(self):
        """Getter method in the above function"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method in the bellow function"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Prints the square itself"""
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
        """Getter method as in the below function"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method as in the below function"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(k) != int for k in value) or any(l < 0 for l in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """Same print behaviour as my_print function"""
        s = ""
        if not self.__size:
            return s
        for a in range(self.__position[1]):
            s += '\n'
        for k in range(self.__size):
            for b in range(self.__position[0]):
                s += ' '
            for l in range(self.__size):
                s += '#'
            s += '\n'
        return s[: - 1]
