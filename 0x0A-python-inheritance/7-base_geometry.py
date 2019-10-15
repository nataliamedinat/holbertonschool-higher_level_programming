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
