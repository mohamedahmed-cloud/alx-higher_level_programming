#!/usr/bin/python3
"""
square - square class that inherit from rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square - is a class that inherit from rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ : this is a constructor used to call super class
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be a positive integer")
        self.__size = size

    def __str__(self):
        """
        __str__ - return a string representation of the object
        """

        return super().__str__("Square")
