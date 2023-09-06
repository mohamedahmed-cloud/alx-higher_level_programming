#!/usr/bin/python3
"""
    say_my_name - function to tell me the name
"""


def say_my_name(first_name="", last_name=""):
    """
    say_my_name - Function to Tell me the name

    args:
        first_name: first user name
        last_name: last user anem
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
