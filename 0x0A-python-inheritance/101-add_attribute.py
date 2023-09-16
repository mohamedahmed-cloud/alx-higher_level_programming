#!/usr/bin/python3

def add_attribute(obj, attribute, value):
    # obj.__dict__[attribute] = value [or]
    setattr(obj, attribute, value)
