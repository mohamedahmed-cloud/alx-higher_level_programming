#!/usr/bin/python3
"""
lookup: return all info about any object
"""


def lookup(obj):
    """
    args:
        obj: the object to get info about it.
    """
    return dir(obj)
