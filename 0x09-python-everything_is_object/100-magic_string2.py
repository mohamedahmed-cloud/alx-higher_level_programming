#!/usr/bin/python3
def magic_string():
    magic_string.call_number = getattr(magic_string,"call_number", 0) + 1
    return ("BestSchool, " * magic_string.call_number)[:-2]
