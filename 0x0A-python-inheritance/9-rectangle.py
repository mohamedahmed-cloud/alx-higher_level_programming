#!/usr/bin/python3
"""
Rectangle: Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle- Rectangle that has an height and width
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self, type = "Rectangle"):
        return f"[{type}] {self.__width}/{self.__height}"
