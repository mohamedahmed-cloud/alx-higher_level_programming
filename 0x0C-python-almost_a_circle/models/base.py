#!/usr/bin/python3
"""
Base class - This class will be the “base” of all other
classes in this project. The goal of it is to manage id
attribute in all your future classes and to
avoid duplicating the same code (by extension, same bugs)
"""


import json


class Base:
    """
     base class - will be the base of all class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string: convert dict to json object.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
