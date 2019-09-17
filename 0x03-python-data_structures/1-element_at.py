#!/usr/bin/python3
def element_at(my_list, idx):
    ln = 0  # Iterator and store the index of the list
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    for a in my_list:
        if (idx == ln):
            return (a)
        ln += 1
