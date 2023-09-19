import unittest, json

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_None(self):
        base = Base()
        self.assertAlmostEqual(base.id, 1)
        base = Base()
        self.assertAlmostEqual(base.id, 2)
        base = Base()
        self.assertAlmostEqual(base.id, 3)
        base = Base()
        self.assertAlmostEqual(base.id, 4)

    def test_value(self):
        # it alread assumed that all value pass is already an integer
        # so we will only test on integer value.
        base = Base(12)
        self.assertAlmostEqual(base.id, 12)
        base = Base(14)
        self.assertAlmostEqual(base.id, 14)
        base = Base(-12)
        self.assertAlmostEqual(base.id, -12)
        base = Base(0)
        self.assertAlmostEqual(base.id, 0)

    def test_to_json_string(self):
        # None value
        val = None
        val = Base.to_json_string(val)
        self.assertEqual(val , "[]")

        # empty dict
        val = {}
        val = Base.to_json_string(val)
        self.assertEqual(val , "[]")

        # have a value1
        val1 = {"x": 12}
        val2 = Base.to_json_string(val1)
        self.assertEqual(val2 , json.dumps(val1))

        # have a value2
        val1 = {"x": 12, "y": 123}
        val2 = Base.to_json_string(val1)
        self.assertEqual(val2 , json.dumps(val1))

    def test_from_json_string(self):
        val1 = {'x':1}
        val2 = Base.to_json_string(val1)
        self.assertEqual(Base.from_json_string(val2), val1)

        val1 = None
        val2 = Base.to_json_string(val1)
        self.assertEqual(Base.from_json_string(val2), [])

        val1 = []
        val2 = Base.to_json_string(val1)
        self.assertEqual(Base.from_json_string(val2), [])


    def test_create(self):
        # Test One
        square = Square.create(**{"size":12})
        self.assertEqual(square.size, 12)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        # Test two
        square = Square.create(**{"size":12, "x": 12, "y": 12})
        self.assertEqual(square.size, 12)
        self.assertEqual(square.x, 12)
        self.assertEqual(square.y, 12)

        # Rectangle
        # Test one
        square = Rectangle.create(**{"width":12, "height": 12})
        self.assertEqual(square.width, 12)
        self.assertEqual(square.height, 12)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        # Test two
        square = Rectangle.create(**{"width":12, "height": 12, "x": 12, "y": 12})
        self.assertEqual(square.width, 12)
        self.assertEqual(square.height, 12)
        self.assertEqual(square.x, 12)
        self.assertEqual(square.y, 12)

    def test_load_from_file(self):
        # file Not found
        # Square 
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        list_rectangles_input = [r1, r2]
        list_rectangles_output = Square.load_from_file()
        self.assertEqual([], list_rectangles_output)

        # Rectangle
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual([], list_rectangles_output)


        # File Found
        # Square 
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        list_rectangles_input = [r1, r2]

        Square.save_to_file(list_rectangles_input)
        list_rectangles_output = Square.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]), str(list_rectangles_input[0]))
        self.assertEqual(str(list_rectangles_output[1]), str(list_rectangles_input[1]))

        # Rectange
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]), str(list_rectangles_input[0]))
        self.assertEqual(str(list_rectangles_output[1]), str(list_rectangles_input[1]))

