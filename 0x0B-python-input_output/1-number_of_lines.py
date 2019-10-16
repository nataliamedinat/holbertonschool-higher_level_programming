#!/usr/bin/python3
def number_of_lines(filename=""):
    """Returns the number of line of a text file
    """
    count = 0
    with open(filename, encoding='utf8') as Myfile:
        for i in Myfile:
            count += 1
    return count
        
