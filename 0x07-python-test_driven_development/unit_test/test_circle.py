import unittest
from circles import area
from math import pi

# python -m unittest filName.py
class TestCircle(unittest.TestCase):
	def test_area(self):
		self.assertAlmostEqual(area(1), 1 * pi)
		self.assertAlmostEqual(area(2), 2 **2 * pi)
	def test_string(self):
		self.assertRaises(ValueError,area, -2)
		self.assertRaises(TypeError, area, "Yousef")
	