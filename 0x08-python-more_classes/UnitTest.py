#!/usr/bin/python3
import unittest
from sys import argv
from unittest.mock import patch

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
        r = Rectangle(10, 10)
        self.assertAlmostEqual(r.area(), 100)
        self.assertAlmostEqual(r.perimeter(), 40)
        r = Rectangle(10)
        self.assertAlmostEqual(r.area(), 0)
        self.assertAlmostEqual(r.perimeter(), 0)
    # 3-rectangle.py
    def test_str(self):
        r = Rectangle(0,0)
        self.assertEqual(str(r), "")
        r = Rectangle(1,2)
        self.assertEqual(str(r), "#\n#")
        r = Rectangle(3,3)
        self.assertEqual(str(r), "###\n###\n###")
    # 4-rectangle.py
    def test_repr(self):
        r = Rectangle(0, 0)
        self.assertEqual(repr(r), "Rectangle(0, 0)")
        r = Rectangle(1,2)
        self.assertEqual(repr(r), "Rectangle(1, 2)")
        r = Rectangle(3, 3)
        self.assertEqual(repr(r), "Rectangle(3, 3)")
    # 5-rectangle.py
    @patch('builtins.print')
    def test_del(self, print):
        r = Rectangle(0, 0)
        del r
        print.assert_called_with("Bye rectangle...")
        r = Rectangle(5, 5)
        del r
        print.assert_called_with("Bye rectangle...")
    # 6-rectangle.py
    def test_class_attribute(self):
        r = Rectangle(0, 0)
        self.assertAlmostEqual(Rectangle.number_of_instances, 1)
        r2 = Rectangle(2, 3)
        r3 = Rectangle(2, 5)
        self.assertAlmostEqual(Rectangle.number_of_instances, 3)
        del r2
        self.assertAlmostEqual(Rectangle.number_of_instances, 2)
    # 7-rectangle.py
    def test_print_symbol(self):
        r  =  Rectangle(1,1)
        r.print_symbol = "Yousef"
        self.assertEqual(str(r), "Yousef")
        r = Rectangle(2, 3)
        r.print_symbol = "Mohamed"
        self.assertEqual(str(r), "MohamedMohamed\nMohamedMohamed\nMohamedMohamed")
    # 8-rectangle.py
    def test_rect_area(self):
        r1 = Rectangle(1,1)
        r2 = "Yousef"
        self.assertRaises(TypeError, lambda: Rectangle.bigger_or_equal(r1, r2))
        r1 = "Yousef"
        r2 = Rectangle(2,2)
        self.assertRaises(TypeError, lambda: Rectangle.bigger_or_equal(r1, r2))

        r1 = Rectangle(2, 3)
        r2 = Rectangle(3, 2)
        self.assertEqual(r1, Rectangle.bigger_or_equal(r1, r2))

        r1 = Rectangle(3, 3)
        r2 = Rectangle(3, 2)
        self.assertEqual(r1, Rectangle.bigger_or_equal(r1, r2))

        r1 = Rectangle(2, 3)
        r2 = Rectangle(3, 3)
        self.assertEqual(r2, Rectangle.bigger_or_equal(r1, r2))

    # 9-rectangle.py
    def test_class_method(self):
        r = Rectangle.square(6)
        assert r.area() == 36
        assert r.perimeter() == 24


