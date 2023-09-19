import unittest, json
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
        # square = Square(1, 1)
        # self.assertEqual(str(square), "[Square] (1) 1/0 - 1")
        # square = Square(10, 12)
        # self.assertEqual(str(square), "[Square] (25) 12/0 - 10")
        # square = Square(12, 10, 12)
        # self.assertEqual(str(square), "[Square] (26) 10/12 - 12")
        square = Square(12, 10, 12, 12)
        self.assertEqual(str(square), "[Square] (12) 10/12 - 12")

    def test_size(self):
        square = Square(1, 1, 12, 12)
        square.size = 24
        self.assertEqual(square.size, 24)
        # value error
        with self.assertRaises(ValueError):
            square.size = -1
        # type error
        with self.assertRaises(TypeError):
            square.size = "Yousef"
        with self.assertRaises(TypeError):
            square.size = True
        with self.assertRaises(TypeError):
            square.size = None
        with self.assertRaises(TypeError):
            square.size = [1, 2]

    def test_update(self):
        s1 = Square(5, 12)
        self.assertEqual(str(s1), "[Square] (37) 12/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 12/0 - 2")
        
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(x=12)
        
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        rectangle = Square(10, 2, 1, 9)
        self.assertEqual(json.dumps(rectangle.to_dictionary()), '{"id": 9, "size": 10, "x": 2, "y": 1}')
        rectangle = Square(12, 12, 12, 12)
        self.assertEqual(json.dumps(rectangle.to_dictionary()), '{"id": 12, "size": 12, "x": 12, "y": 12}')