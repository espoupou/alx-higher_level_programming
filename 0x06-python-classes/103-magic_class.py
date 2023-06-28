#!/usr/bin/python3
"""magic class file
"""
import math


class MagicClass:
    """Class MAGIC
    """

    def __init__(self, radius=0):
        """ init class
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ calculates the area """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """ calculates the perimeter """
        return (2 * math.pi * self.__radius)
