#!/usr/bin/python3
import json


def from_json_string(my_str):
    """Returns an object(Python) represented by a JSON str
    """
    return json.loads(my_str)
