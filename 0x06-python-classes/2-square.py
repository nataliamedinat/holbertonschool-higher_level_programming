#!/usr/bin/python3
class Square:
    """Define a Square class
    """

    def __init__(self, size=0):

        """TypeError: size must be an integer
        ValueError: size less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
