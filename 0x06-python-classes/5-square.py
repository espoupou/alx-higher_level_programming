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

    def area(self):
        """ square area calculation
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ returns the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ prints a square with #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
