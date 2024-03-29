#!/usr/bin/python3
"""
Say My Name - function that says your name.
"""


def say_my_name(first_name, last_name=""):
    """
    Says your name.
    first_name and last_name must be strs otherwise, will raise a TypeError
    """
    # first_name must be an str
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    # last_name must be an str
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
