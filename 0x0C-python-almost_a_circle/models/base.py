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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file:  that writes the JSON string
        representation of list_objs to a file:
        """
        name = cls.__name__
        file_name = f"{name}.json"
        store = []
        with open(file_name, "w", encoding='utf-8') as f:
            if list_objs is not None:
                for obj in list_objs:
                    store.append(obj.to_dictionary())
                # print(store)
            f.write(cls.to_json_string(store))

    @staticmethod
    def from_json_string(json_string):
        """
        that returns the list of the JSON string representation json_string:
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
         create: returns an instance with all attributes already set:
        """

        from models.rectangle import Rectangle
        from models.square import Square

        className = cls.__name__
        if className == "Rectangle":
            # width=0, height=0, x=0, y=0, id=None
            [width, height, x, y, id] = [dictionary.get("width"),
                                         dictionary.get("height"),
                                         dictionary.get("x"),
                                         dictionary.get("y"),
                                         dictionary.get("id")]
            return Rectangle(width, height, x, y, id)
        else:
            [size, x, y, id] = [dictionary.get("size"), dictionary.get("x"),
                                dictionary.get("y"), dictionary.get("id")]
            return Square(size, x, y, id)
