#!/usr/bin/python3
""" Module contain a definition for Square Class"""


class Square:
    """
        This is the square class.
    """
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def __lt__(self, other) -> bool:
        return self.size < other.size

    def __gt__(self, other) -> bool:
        return self.size > other.size

    def __eq__(self, other) -> bool:
        return self.size == other.size

    def __ne__(self, other) -> bool:
        return self.size != other.size

    def __ge__(self, other) -> bool:
        return self.size >= other.size

    def __le__(self, other) -> bool:
        return self.size <= other.size
