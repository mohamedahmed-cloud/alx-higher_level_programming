#!/usr/bin/python3
"""
unit test for max integer function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    # def test_type_value(self):
    #     self.assertRaises(TypeError, max_integer, "Yousef")
    #     self.assertRaises(TypeError, max_integer, ["Yousef"])
    #     self.assertRaises(TypeError, max_integer, [True, 1, 3])
    #     self.assertRaises(TypeError, max_integer, [["list", 1], 3, 4])
    #     self.assertRaises(TypeError, max_integer, {1, 2, 3})
    #     self.assertRaises(TypeError, max_integer, {2: "yousef", 3: "Ahmed"})
    #     self.assertRaises(TypeError, max_integer, [1, 2, 4, 4+5j, 5+8j])

    def test_correct_answer(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, -4, -5, -6]), 1)
        self.assertAlmostEqual(max_integer([-1, 4, 3, 5]), 5)
        self.assertAlmostEqual(max_integer([-1, 0, 3.4, 9]), 9)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([300000000000]), 300000000000)
        self.assertAlmostEqual(max_integer([-1]), -1)
        self.assertAlmostEqual(max_integer([-1, -2]), -1)
