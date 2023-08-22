#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deleted_key = []
    for key, val in a_dictionary.items():
        if val == value:
            deleted_key.append(key)
    for x in deleted_key:
        del a_dictionary[x]
    return a_dictionary
