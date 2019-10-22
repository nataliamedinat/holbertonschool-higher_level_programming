#!/usr/bin/python3
""" Module for Base class
"""
import json


class Base:
    """Define a class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Returns the json representation """
        if list_dictionaries is None or list_dictionaries == 0:
            return("[]")
        else:
            return json.dumps(list_dictionaries)
