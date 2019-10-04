#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """define a class aquare
        """
        self.__size = size

    @property
    def size(self):
        """
        """
        return self.__size

    @size.setter
    def size(self, value):
        """TypeError: if size is not an integer
           ValueError: if size is less than zero
        """
        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns area of size by size
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints empty line
        """
        if self.__size == 0:
            print()
        else:
            for column in range(self.__size):
                for row in range(self.__size):
                    print('#', end="")
                print()
