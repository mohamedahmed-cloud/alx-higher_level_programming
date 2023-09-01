#!/usr/bin/python3
class OurClass:
    def __init__(self, a):
        self.x = a
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x < 1000:
            self.__x = 1000
        else:
            self.__x = x


Classes = OurClass(10)
print(Classes.__dict__)
# decorators:
"""
@classmethod
@property
@attribute.setter
"""


