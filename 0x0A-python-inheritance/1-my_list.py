#!/usr/bin/python3
class MyList(list):
    """Class that inherits from list
    """
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """Prints the sorted list
        """
        print(sorted(self))
