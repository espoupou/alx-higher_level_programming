#!/usr/bin/python3
"""Module that define a Square class.
"""


class Square:
    """class Square that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize method that stores the size of the square

        Args:
            size (int): size of the square
            position (int, int): square position in space
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """ Method that returns the position value
        """
        return self.__position

    @position.setter
    def position(self, value=(0, 0)):
        """ sets the position value
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ prints a square with # in space
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()

            for i in range(self.__size):
                for j in range(self.position[0]):
                    print(" ", end='')

                for j in range(self.__size):
                    print("#", end='')
                print()

    def __str__(self):
        """class string
        """
        string = ""
        if self.__size == 0:
            return "\n"
        else:
            for i in range(self.position[1]):
                string += "\n"

            for i in range(self.__size):
                for j in range(self.position[0]):
                    string += " "

                for j in range(self.__size):
                    string += "#"
                string += "\n"
            return string
