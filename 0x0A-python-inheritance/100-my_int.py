#!/usr/bin/python3
"""
MyInt - int class that inherit from int python class
"""

class MyInt(int):
    def __eq__(self, other):
           return self != other

    def __ne__(self, other):
        return self == other
