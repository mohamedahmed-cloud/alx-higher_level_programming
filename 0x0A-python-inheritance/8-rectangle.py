#!/usr/bin/python3
"""
BaseGeometry: BaseGeometry class
"""


class BaseGeometry:
    """
        BaseGeometry class - area class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name=-float("inf"), value=-float("inf")):
        if value == -float("inf") or name == -float("inf"):
            return
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
        Rectangle- Rectangle that has an height and width
    """
    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
