#!/usr/bin/python3
def uppercase(str):
    for cont in (str):
        if ord(cont) > 96 and ord(cont) < 123:
            cont = chr(ord(cont) - 32)
        print("{}".format(cont), end="")
    print("")
