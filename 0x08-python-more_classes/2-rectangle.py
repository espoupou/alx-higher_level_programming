#!/usr/bin/python3
"""Module that define a Rectangle
"""


class Rectangle:
    """Class Square that defines a Rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle

               Args:
                   width (int): width
                   height (int): height
               """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = int(width)

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = int(height)

    @property
    def width(self):
        """ returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
