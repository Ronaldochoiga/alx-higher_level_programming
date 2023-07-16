#!/usr/bin/python3
"""
This is the add module.
adds 2 integers
i and j must be first casted
"""


def add_integer(i, j=98):
    """i and are ints
    Returns an int: the add of i and j
    """
    if isinstance(i, float):
        i = int(i)
    if isinstance(j, float):
        j = int(j)
    if not (isinstance(i, int)):
        raise TypeError("i must be an integer")
    if not (isinstance(j, int)):
        raise TypeError("j must be an integer")
    return (i + j)
