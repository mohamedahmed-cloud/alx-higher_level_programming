#!/usr/bin/python3
"""
script that adds all arguments to a
Python list, and then save them to a file:
"""


from sys import argv


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file_name = "add_item.json"
res = []

if __name__ == "__main__":
    try:
        res = load_from_json_file(file_name)
    except Exception:
        pass

    res.extend(argv[1:])
    save_to_json_file(res, file_name)
