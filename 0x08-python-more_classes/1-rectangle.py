#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        """Define a Rectangle class
           Arguments:
           @width: Width of the rectangle
           @height: height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Property to width to retrieve it
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) != int is False:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Property to height to retieve it
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ TypeError: If height is not an integer
            ValueError: if height is less than 0
        """
        if type(value) != int is False:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
