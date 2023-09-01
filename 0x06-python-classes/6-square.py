#!/usr/bin/python3
""" Module contain a definition for Square Class"""


class Square:
    """
        This is the square class.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    def my_print(self):
        for i in range(self.size):
            print(" " * self.position[0]+"#"*self.size)
        if self.size == 0:
            print()

    # position attribute.
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
