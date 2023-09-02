#!/usr/bin/python3
import math


class MagicClass:
    """ magic Class Function"""
    def __init__(self, radius):
        self.__radius = radius

    """Setter Method for radius"""
    def radius(self, radius):
        if not isinstance(radius, int) or not isinstance(radius, float):
            TypeError("radius must be a number")
        self.__radius = radius

    """get aread of circle"""
    def area(self):
        return self.__radius ** 2 * math.pi

    """get perimeter of circle"""
    def circumference(self):
        return 2 * math.pi * self.__radius
