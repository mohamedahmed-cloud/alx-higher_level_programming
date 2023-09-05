#!/usr/bin/python3
import unittest
from sys import argv

className = argv[-1][2:-3].capitalize()
module = __import__(argv[-1][:-3])
Rectangle = getattr(module, className)


class RectangleTest(unittest.TestCase):
    # 0-rectangle.py
    def test_isInstance(self):
        r = Rectangle()
        self.assertIsInstance(r, Rectangle)

    # 1-rectangle.py test
    def test_CheckValue(self):
        r = Rectangle(1,3)
        self.assertAlmostEquals(r.width, 1)
        self.assertAlmostEquals(r.height, 3)
        self.assertRaises(ValueError, lambda: Rectangle(-2, 1))
        self.assertRaises(ValueError, lambda: Rectangle(2, -1))
        self.assertRaises(TypeError, lambda: Rectangle(2, "Yousef"))
        self.assertRaises(TypeError, lambda: Rectangle("Yousef", 1))

    # 2-rectangle.py test 
    def test_area_perimeter(self):
        r = Rectangle(3,4)
        self.assertAlmostEqual(r.area(), 12)
        self.assertAlmostEqual(r.perimeter(), 14)
        r = Rectangle(0,0)
        self.assertAlmostEqual(r.area(), 0)
        self.assertAlmostEqual(r.perimeter(), 0)

