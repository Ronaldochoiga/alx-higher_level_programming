#!/usr/bin/python3
"""
Print Square module, for printing squares with "#".

"""


def print_square(size):
    """
    size is the size length of the square

    """


    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')


    for x in range(size):
        print('#' * size)
