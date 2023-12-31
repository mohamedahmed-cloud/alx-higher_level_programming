#!/usr/bin/python3

"""
Magic Class Implementation.
"""

import math


class MagicClass:
    """
    A magical class that performs calculations on a circle.

    Attributes:
        __radius (float): The radius of the circle.

    Methods:
        __init__(self, radius): Initializes a MagicClass instance with a
        given radius.
        radius(self, radius): Setter method to set the radius
        of the circle.
        area(self): Calculate and return the area of the circle.
        circumference(self): Calculate and return the circumference
        of the circle.
    """
    def __init__(self, radius=0):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate and return the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
