#!/usr/bin/python3
"""
from_json_string:   function that returns an object
                    (Python data structure) represented
                    by a JSON string
"""

import json


def from_json_string(my_str):
    """
    args:
        my_str: json object need to convert to python object.
    """
    return json.loads(my_str)
