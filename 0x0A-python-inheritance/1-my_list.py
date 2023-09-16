#!/usr/bin/python3
"""
MyList: class that inherit from list class
        this class is used to print the sorted list in python.
"""


class MyList(list):
    """
        args:
            list : list to print the sorted list
    """
    def print_sorted(self):
        print(sorted(self))
