#!/usr/bin/python3
class BaseGeometry:
    """Define a BaseGeometry class
    """
    def area(self):
        """Public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """TypeError: If value is not an integer
           ValueError: If value is less or equal to 0
        """
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Define a class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):

        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height

    def area(self):
        """Return the area
        """
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """Define a Square class that inherits from Rectangle
    """
    def __init__(self, size):

        self.integer_validator('size', size)
        self.__size = size

        super().__init__(self.__size, self.__size)
