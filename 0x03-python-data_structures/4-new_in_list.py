#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ln = 0
    new_list = []
    if idx < 0:
        return (my_list.copy())
    if idx >= len(my_list):
        return (my_list.copy())
    new_list = my_list.copy()  # Making the copy of the list
    for a in my_list:
        if idx == ln:
            new_list[ln] = element
            return (new_list)
        ln += 1
