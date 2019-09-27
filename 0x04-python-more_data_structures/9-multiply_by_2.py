#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()  # Making the copy of the dictionary
    for key in a_dictionary:
        new_dictionary[key] = new_dictionary[key] * 2
    return (new_dictionary)
