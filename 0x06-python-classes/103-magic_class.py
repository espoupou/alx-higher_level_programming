#!/usr/bin/python3
from math import pi


class MagicClass:

    """Class that stores the properties
    of a circumference"""
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = 0

    def area(self):
        """ Method that calculates the area of the circumference """
        return ((self.__radius ** 2) * pi)

    def circumference(self):
        """ Method that calculates the perimeter of a circumference """
        return (2 * pi * self.__radius)
