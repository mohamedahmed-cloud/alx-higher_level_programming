#!/bin/usr/python3
"""
inherits_from - function that returns True if the object is an
    instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    args:
        obj: object to compare a_class paramters
        a_class: class to compare against
    """
    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
