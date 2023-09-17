#!/usr/bin/python3
"""
read_file: function that reads a text file (UTF8) 
    and prints it to stdout:
"""


def read_file(filename=""):
    """
    filename - the file name passed to 
    read data from it
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
