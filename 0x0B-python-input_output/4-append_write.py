#!/usr/bin/python3
def append_write(filename="", text=""):
    """Appends a string at the end of a text
    """
    with open(filename, mode='a', encoding='utf8') as myFile:
        return myFile.write(text)
