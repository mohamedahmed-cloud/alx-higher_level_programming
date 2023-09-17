#!/usr/bin/python3

"""
load_from_json_file:    function that creates an
                        Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
    args:
        filename: file need to read from it.
    """
    with open(filename, "r", encoding="utf-8") as file:
        store = file.read()
        return json.dumps(store)
