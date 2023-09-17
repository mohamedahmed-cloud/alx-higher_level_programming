#!/usr/bin/python3
"""
to_json_string:  function that returns the JSON
                 representation of an object (string):
"""


import json


def to_json_string(my_obj):
    """
    args:
        my_obj: the object need to make a seralize for it.
    """
    json_obj = json.dumps(my_obj)
    # print(type(json_obj))
    return json_obj
