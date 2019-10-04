#!/usr/bin/python3
"""Function that adds two values, checks if they are numbers,
 casts them as ints and returns the result of their addition
    Args:
    a: First number to added, user input
    b: Second number to added, user input
"""


def add_integer(a, b=98):

    """ Function that adds 2 integers
          Return the addition of the two numbers
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
