#!/usr/bin/python3
"""Defines a class MagicClass"""
import math


class MagicClass:
    """
    Class that defines properties of MagicClass.
    Attributes:
        radius: radius.
    """
    def __init__(self, radius=0):
        """Creates new instance
        Args:
            radius: radius.
        Raises:
            TypeError showing radius must be a number
        """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Returns area
        Returns: area of the circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Returns circumference
        Returns: circumference of the circle.
        """
        return 2 * math.pi * self.__radius
