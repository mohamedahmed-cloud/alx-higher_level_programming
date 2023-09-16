#!/usr/bin/python3
"""
add_attribute - implementation the function that can
    add attribute to curr object
"""


def add_attribute(obj, attribute, value):
    """
    args:
     1. obj - curr object to add attributes
     2. attribute - attribute name
     3. value - attribute value
    """
    # obj.__dict__[attribute] = value [or]
    setattr(obj, attribute, value)
