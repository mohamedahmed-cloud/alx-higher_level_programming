#!/usr/bin/python3
"""
script that adds all arguments to a
Python list, and then save them to a file:
"""


from sys import argv


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
file_name = "add_item.json"


save_to_json_file(argv[1:], file_name)

load_from_json_file(file_name)
