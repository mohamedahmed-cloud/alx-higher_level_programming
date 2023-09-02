#!/usr/bin/python3
"""Magic Class Implementation."""


import math


class MagicClass:
    """ magic Class Function"""
    def __init__(self, radius):
        self.__radius = radius

    @radius.setter
    def radius(self, radius):
        if not isinstance(radius, int) or not isinstance(radius, float):
            TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.radius
