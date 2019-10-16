#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file utf8
    """
    with open(filename, encoding='utf8') as Myfile:
        print(Myfile.read(), end='')
