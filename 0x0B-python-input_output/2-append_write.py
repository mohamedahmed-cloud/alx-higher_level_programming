#!/usr/bin/python3

"""
append_write -  function that appends a string at
                the end of a text file (UTF8) and returns
                the number of characters added:
"""


def append_write(filename="", text=""):
    """
    args:
        filename: file to append text on it
        text: text needed to appending in the file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
