#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Define a class Rectangle
           Arguments:
           @width: Width of the rectangle
           @height: height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Property to width to retrieve it
        """
        return self.__width

    @width.setter
    def width(self, value):
        """TypeError: If width is not an integer
           ValueError: If width is less than 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Property to height to retrieve it
        """
        return self.__height

    @height.setter
    def height(self, value):
        """TypeError: If height is not an integer
           ValueError: if height is less than 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        # Calculates and returns the rectangle area
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and return the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (((self.__width) + (self.__height)) * 2)

    def __str__(self):
        """Method that creates a new string object from the given object
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string

        for a in range(self.__height):
            string += str(self.print_symbol) * self.__width

            if a < (self.__height - 1):
                string += "\n"
        return string

    def __repr__(self):
        """Return a string representation of the rectangle
           new instance using eval()
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Special method of a class, destructor method
        """
        print("Bye rectangle...")
        type(self).number_of_instances += -1
