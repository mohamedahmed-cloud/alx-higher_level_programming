#!/usr/bin/python3

"""
append_after - function that inserts a line of text to a file,
 after each line containing a specific string (see example):
"""


def append_after(filename="", search_string="", new_string=""):
    """
    args:
        filename: the file read and write from it
        search_string: the string to search for in filename
        new_string: the string to insert after each line
        containing search_string
    Return:
        filename: modified file name
    """
    with open(filename, 'r+', encoding="utf-8") as file:
        res = ""
        for line in file:
            res += line
            if search_string in line:
                res += new_string
        file.seek(0)
        file.truncate()
        file.write(res)
