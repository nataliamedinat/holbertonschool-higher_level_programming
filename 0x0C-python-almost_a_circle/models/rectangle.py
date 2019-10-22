#!/usr/bin/python3
from models.base import Base
""" Module for rectangle class """


class Rectangle(Base):
    """Class rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor
            Args:
            @width: Width Rectangle
            @height: Height rectangle
            @x: Position x
            @y: Position y
            @id: Instances
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Property to width to retrieve it """
        return self.__width

    @width.setter
    def width(self, value):
        """ TypeError: If its not an int
            ValueError: If is less or equal to 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Property to width to retrieve it """
        return self.__height

    @height.setter
    def height(self, value):
        """ TypeError: If its not an int
            ValueError: If is less or equal to 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Property to width to retrieve it """
        return self.__x

    @x.setter
    def x(self, value):
        """ TypeError: If its not an int
            ValueError: If is less than 0
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Property to width to retrieve it """
        return self.__y

    @y.setter
    def y(self, value):
        """ TypeError: If its not an int
            ValueError: If is less than 0
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """Method that prints in stdout the rectangle with #
        """
        for b in range(self.__y):
            print()
        for i in range(self.__height):
            print(self.__x * " ", end="")
            for a in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """Returns a string
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """ Internal Method that assigns an argument to each attribute"""
        if id is not None:
            self.id = id

        if width is not None:
            self.width = width

        if height is not None:
            self.height = height

        if x is not None:
            self.x = x

        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Assigns arguments to each attribute no-keyword and keyword"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
