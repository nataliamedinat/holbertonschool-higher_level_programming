#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """define a class square
        """
        self.__size = size

    @property
    def size(self):
        """
        """
        return self.__size

    @size.setter
    def size(self, value):
        """         TypeError: if size is not an integer
                    ValueError: if size is less than zero
        """
        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns area of the square
        """
        return self.__size * self.__size
