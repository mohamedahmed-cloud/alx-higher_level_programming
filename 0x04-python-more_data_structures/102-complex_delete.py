#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    shallowCopy = a_dictionary.copy()
    for key, val in a_dictionary.items():
        if val == value:
            del shallowCopy[key]
    return shallowCopy
