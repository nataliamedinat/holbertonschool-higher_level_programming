#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """Reads n lines of  atext file and prints it
    """
    count = 0
    with open(filename, encoding="utf8") as myFile:
        for line in myFile:
            if nb_lines < 0 or nb_lines == 0 or nb_lines > count:
                print(line, end="")
                count += 1
