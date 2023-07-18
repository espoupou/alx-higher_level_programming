#!/usr/bin/python3
""" Module that contains class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes instances """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ overriding the __str__ method """
        string = "[Square] "
        string += "({}) ".format(self.id)
        string += "{}/{} - ".format(self.x, self.y)
        string += "{}".format(self.size)
        return string

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary reprensation """
        atribs = ['id', 'x', 'size', 'y']
        dico = {}

        for key in atribs:
            if key == 'size':
                dico[key] = getattr(self, 'width')
            else:
                dico[key] = getattr(self, key)
        return dico
