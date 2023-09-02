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

    def __str__(self):
        result = ""
        if self.size:
            result += "\n" * (self.position[1] - 1)
        for i in range(self.size):
            result += (" " * self.position[0]+"#"*self.size) + "\n"
        if self.size == 0:
            result += "\n"

        return result

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, int) or len(value) != 2 \
          or not isinstance(value[1], int) or not isinstance(value[0], int) \
          or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
