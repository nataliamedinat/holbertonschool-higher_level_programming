#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    array = []
    for i in my_list:
        if i % 2 == 0:
            array.append(True)
        else:
            array.append(False)
    return (array)
