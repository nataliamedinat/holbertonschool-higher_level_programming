#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    ln = 0
    if idx < 0:
        return (my_list)
    if idx >= len(my_list):
        return (my_list)
    for a in my_list:
        if idx == ln:
            my_list[ln] = element
            return (my_list)
        ln += 1
