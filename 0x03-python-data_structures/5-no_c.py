#!/usr/bin/env python3
def no_c(my_string):
    string = ""
    for a in my_string:
        if a == 'c' or a == 'C':
            continue
        string = string + a
    return (string)
