#!/usr/bin/python3
""" Module only contain a definition for Square Class"""


class Square:
    """
        This is the square class.
    """
    def __init__(self, size=0):
        try:
            if isinstance(size, int):
                if size >= 0:
                    self.__size = size
                else:
                    raise ValueError
            else:
                raise TypeError
        except TypeError:
            print("size must be an integer")
            raise
        except ValueError:
            print("size must be >= 0")
            raise
