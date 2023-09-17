#!/usr/bin/python3
"""
save_to_json_file: function that writes an Object to a
                   text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    args:
        my_obj: object to writen in text file
        filename: the file that object will writen in it.
    """
    with open(filename, "w", encoding="utf-8") as file:
        text = json.dumps(my_obj)
        file.write(text)
