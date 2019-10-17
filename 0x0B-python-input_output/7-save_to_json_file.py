#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file
    """
    with open(filename, mode='w', encoding="utf8") as myFile:
        json.dump(my_obj, myFile)
