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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the json representation """

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Method that writes the json string representation
            of list_objs to a file.
        """

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the json strinf representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
           Args:
          @cls: Current class
          @dictionary: Like a double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1, 0, 0)
        elif cls.__name__ == "Square"
            new_instance = cls(1, 0, 0)
        new_instance.update(**dictionary)
        return new_instance

    def load_from_file(cls):
        """ Return a list of instances """
        
