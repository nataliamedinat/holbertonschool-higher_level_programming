#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """Creates an object from json file
    """
    with open(filename, encoding="utf8") as myObject:
        return json.load(myObject)
