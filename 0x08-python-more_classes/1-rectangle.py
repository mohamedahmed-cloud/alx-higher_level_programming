#!/usr/bin/python3
"""
Rectangle - is a Rectangle Class
"""


class Rectangle:
    """
        Rectangle Class - Implementation of Class Rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    #Width Getter and Setter 
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            TypeError("width must be an integer")
        elif value < 0:
            ValueError("width must be >= 0")
        self.__width = value
    
    # height getter and setter
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) is not int:
            TypeError("height must be an integer")
        elif value < 0:
            ValueError("height must be >= 0")
        self.__height = value
        

