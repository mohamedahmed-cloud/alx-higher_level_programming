#!/usr/bin/python3
"""
unit test for max integer function.
"""

import unittest
max_integer = __import__("main").max_integer


class MaxIntegerTest(unittest.TestCase):
    def test_type_value(self):
        self.assertRaises(TypeError, max_integer, "Yousef")
        self.assertRaises(TypeError, max_integer, ["Yousef"])
        self.assertRaises(TypeError, max_integer, [True, 1, 3])
        self.assertRaises(TypeError, max_integer, [["list", 1], 3, 4])
        self.assertRaises(TypeError, max_integer, {1, 2, 3})
        self.assertRaises(TypeError, max_integer, {2: "yousef", 3: "Ahmed"})
        self.assertRaises(TypeError, max_integer, [1, 2, 4, 4+5j, 5+8j])

    def test_correct_answer(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, -4, -5, -6]), 1)
        self.assertAlmostEqual(max_integer([-1, 0, 3.4, 5.6]), 5.6)
