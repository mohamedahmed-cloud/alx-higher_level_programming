#!/usr/bin/python3
"""
Rectangle - is a Rectangle Class
"""


class Rectangle:
    """
        Rectangle Class - Implementation of Class Rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # Width Getter and Setter
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # height getter and setter
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if not self.height or not self.width:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        if not self.width or not self.height:
            return ""
        return (("#" * self.width + "\n") * self.height)[:-1]
    def __repr__(self):
        if not self.width or not self.height:
            return ""
        return (("#" * self.width + "\n") * self.height)[:-1]
