#!/usr/bin/python3
"""
is_kind_of_class: class check the type of of a class
"""


def is_kind_of_class(obj, a_class):
    """
    args:
    obj: object to check it's type
    a_class: class to compare with obj arguments
    """
    return isinstance(obj, a_class)
