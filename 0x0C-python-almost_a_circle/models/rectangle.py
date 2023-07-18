#!/usr/bin/python3
""" Module that contains class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instances """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of rectangle """
        return self.width * self.height

    def display(self):
        """ displays a rectangle """
        array = self.y * "\n"
        for i in range(self.height):
            array += (" " * self.x)
            array += ("#" * self.width) + "\n"
        print(array, end='')

    def __str__(self):
        """ overriding the __str__ method """
        string = "[Rectangle] "
        string += "({}) ".format(self.id)
        string += "{}/{} - ".format(self.x, self.y)
        string += "{}/{}".format(self.width, self.height)
        return string

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) != 0:
            atribs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, atribs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ method that returs a dictionary representation """
        atribs = ['x', 'y', 'id', 'height', 'width']
        dico = {}

        for key in atribs:
            dico[key] = getattr(self, key)
        return dico
