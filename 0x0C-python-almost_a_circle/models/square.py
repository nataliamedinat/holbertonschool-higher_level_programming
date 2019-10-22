#!/usr/bin/python3
""" Module for square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square inherit from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

    def __update(self, id=None, size=None, x=None, y=None):
        """ Internar method that updates attributes """
        if id is not None:
            self.id = id

        if size is not None:
            self.size = size

        if x is not None:
            self.x = x

        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Assigns attributes """
        if args:
            self.__update(*args)

        if kwargs:
            self.__update(**kwargs)
