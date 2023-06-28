#!/usr/bin/python3
"""Module that define a Square class.
"""


class Square:
    """class Square that defines a square
    """
    def __init__(self, size=0):
        """Initialize method that stores the size of the square

        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
