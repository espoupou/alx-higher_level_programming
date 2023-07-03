#!/usr/bin/python3
"""Module that define a Rectangle
"""


class Rectangle:
    """Class Square that defines a Rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

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

        Rectangle.number_of_instances += 1

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
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """class string
        """
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += Rectangle.print_symbol
            if i < self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """string representation to recreate instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """todo on delete
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare two rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """create a square from rectangle
        """
        return cls(size, size)
