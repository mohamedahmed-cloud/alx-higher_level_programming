#!/usr/bin/python3

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x},{self.y})'

obj = Point2D(2, 3)
print(obj.__slots__)
print(Point2D.__dict__)