#!/usr/bin/python3
"""
MyInt - int class that inherit from int python class
"""


class MyInt(int):
    """
    MyInt - int class that inherit from int python class
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
