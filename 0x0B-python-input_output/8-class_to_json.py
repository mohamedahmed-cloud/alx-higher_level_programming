#!/usr/bin/python3

"""
class_to_json: function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object:
"""


import json


def class_to_json(obj):
    """
    args:
       obj: object to be serialized
    """
    print(obj)
    return json.dumps(obj.__dict__)
