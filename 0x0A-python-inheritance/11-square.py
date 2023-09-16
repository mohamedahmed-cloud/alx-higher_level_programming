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
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return super().area()

    def __str__(self):
        return super().__str__("Square")
