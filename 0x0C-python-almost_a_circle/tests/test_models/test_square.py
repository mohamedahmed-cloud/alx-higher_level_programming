import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        # test all value pass
        square = Square(20, 20, 20, 1)
        self.assertEqual(square.width, 20)
        self.assertEqual(square.height, 20)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 20)
        self.assertEqual(square.id, 1)
        # test value error
        # value error with width and height
        with self.assertRaises(ValueError):
            square = Square(-1).width
        with self.assertRaises(ValueError):
            square = Square(0).height
        with self.assertRaises(ValueError):
            square = Square(-1).x
        # value error with x and y
        with self.assertRaises(ValueError):
            square = Square(1, -1).x
        with self.assertRaises(ValueError):
            square = Square(1, -1).y


        # test type error
        # type error with width and height
        with self.assertRaises(TypeError):
            square = Square("Yousef").width
        with self.assertRaises(TypeError):
            square = Square(True).width
        with self.assertRaises(TypeError):
            square = Square(None).width
        with self.assertRaises(TypeError):
            square = Square([1, 2]).width

        # height
        with self.assertRaises(TypeError):
            square = Square("Yousef").height
        with self.assertRaises(TypeError):
            square = Square(True).height
        with self.assertRaises(TypeError):
            square = Square(None).height
        with self.assertRaises(TypeError):
            square = Square([1, 2]).height

        # x
        with self.assertRaises(TypeError):
            square = Square(1, "Yousef").x
        with self.assertRaises(TypeError):
            square = Square(123, True).x
        with self.assertRaises(TypeError):
            square = Square(12, None).x
        with self.assertRaises(TypeError):
            square = Square(123, [1, 2]).x

        # y
        with self.assertRaises(TypeError):
            square = Square(1, 1, "Yousef").y
        with self.assertRaises(TypeError):
            square = Square(123, 1,True).y
        with self.assertRaises(TypeError):
            square = Square(12, 1, None).y
        with self.assertRaises(TypeError):
            square = Square(123, 1, [1, 2]).y
    def test_str(self):
        square = Square(1, 1)
        self.assertEqual(str(square), "[Square] (24) 1/0 - 1")
        square = Square(10, 12)
        self.assertEqual(str(square), "[Square] (25) 12/0 - 10")
        square = Square(12, 10, 12)
        self.assertEqual(str(square), "[Square] (26) 10/12 - 12")
        square = Square(12, 10, 12, 12)
        self.assertEqual(str(square), "[Square] (12) 10/12 - 12")
    