#!/usr/bin/python3
import unittest
from sys import argv

className = argv[-1][2:-3].capitalize()
module = __import__(argv[-1][:-3])
Rectangle = getattr(module, className)


class RectangleTest(unittest.TestCase):
    def test_isInstance(self):
        r = Rectangle()
        self.assertIsInstance(r, Rectangle)



