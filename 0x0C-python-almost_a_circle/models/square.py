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
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def __str__(self):
        """
        __str__ - return a string representation of the object
        """

        return super().__str__("Square")

    def update(self, *args, **kwargs):
        """
        update - this is a method used to update the object attributes
        """
        args = list(args)
        if len(args) >= 2:
            args.insert(2, args[1])

        if kwargs.get("size"):
            kwargs["width"] = kwargs.get("size")
            kwargs["height"] = kwargs.get("size")
            del kwargs["size"]

        super().update(*args, **kwargs)

    def to_dictionary(self):
        """
        to_dictionary - provide a dictionary representation for the object.
        """
        return super().to_dictionary("Square")
