#!/usr/bin/python3
"""
Square - square class that inherit from Rectangle Class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
        Square -> square class that inherit from Rectangle
    """
    def __init__(self, size):
        super().__init__(size, size)

    def area(self):
        return super().area()
