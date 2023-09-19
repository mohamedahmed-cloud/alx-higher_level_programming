import unittest, json
from unittest.mock import patch
from io import StringIO
# import rectangle
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_getter(self):
        # test initial condition
        with self.assertRaises(ValueError):
            Rectangle().width
        with self.assertRaises(ValueError):
            Rectangle().height
        self.assertAlmostEqual(Rectangle(1, 1).x, 0)
        self.assertAlmostEqual(Rectangle(1, 1).y, 0)
        
        # give negative value for width and height
        with self.assertRaises(ValueError):
            Rectangle(-1, 1).width
        with self.assertRaises(ValueError):
            Rectangle(1, -1).height
        self.assertAlmostEqual(Rectangle(1, 1).x, 0)
        self.assertAlmostEqual(Rectangle(1, 1).y, 0)

        # give 0 value for width and height
        with self.assertRaises(ValueError):
            Rectangle(0, 3).width
        with self.assertRaises(ValueError):
            Rectangle(3, 0).height
        self.assertAlmostEqual(Rectangle(1, 1).x, 0)
        self.assertAlmostEqual(Rectangle(1, 1).y, 0)

        # give value foor all Rectangle __init__ parameters
        # give x and y negative value
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1, 1).x
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1).y
        
        # give value foor all Rectangle __init__ parameters
        rectangle = Rectangle(1, 1, 1, 1)
        self.assertAlmostEqual(rectangle.width, 1)
        self.assertAlmostEqual(rectangle.height, 1)
        self.assertAlmostEqual(rectangle.x, 1)
        self.assertAlmostEqual(rectangle.y, 1)

        # check on type
        # type of width
        with self.assertRaises(TypeError):
            Rectangle("Yousef", 1, 1, 1).width
        with self.assertRaises(TypeError):
            Rectangle(1, "Yousef", 1, 1).height
        with self.assertRaises(TypeError):
            Rectangle(1, 1, "Yousef", 1).x
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, "Yousef").y

    def test_area(self):
        rectangle = Rectangle(2, 4, 1, 1)
        self.assertAlmostEqual(rectangle.area(), 8)
        rectangle = Rectangle(1, 1, 1, 1)
        self.assertAlmostEqual(rectangle.area(), 1)
        rectangle = Rectangle(10, 20, 1, 1)
        self.assertAlmostEqual(rectangle.area(), 200)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_small(self, mock):
        rectangle1 =Rectangle(1, 1)
        rectangle1.display()
        excepted_value1 = mock.getvalue()
        self.assertEqual(excepted_value1,"#\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_medium(self, mock):
        rectangle2 =Rectangle(2, 3)
        rectangle2.display()
        excepted_value2 = mock.getvalue()
        self.assertEqual(excepted_value2,"##\n##\n##\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_large(self, mock):
        rectangle2 =Rectangle(10, 3)
        rectangle2.display()
        excepted_value2 = mock.getvalue()
        self.assertEqual(excepted_value2,"##########\n##########\n##########\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_according_to_x_y_one(self, mock):
        rectangle3 =Rectangle(10, 3, 1, 1)
        rectangle3.display()
        excepted_value2 = mock.getvalue()
        self.assertEqual(excepted_value2,"\n ##########\n ##########\n ##########\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_according_to_x_y_two(self, mock):
        rectangle3 =Rectangle(10, 3, 0, 3)
        rectangle3.display()
        excepted_value2 = mock.getvalue()
        self.assertEqual(excepted_value2,"\n\n\n##########\n##########\n##########\n")
    
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_according_to_x_y_three(self, mock):
        rectangle3 =Rectangle(10, 3, 3, 0)
        rectangle3.display()
        excepted_value2 = mock.getvalue()
        self.assertEqual(excepted_value2,"   ##########\n   ##########\n   ##########\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_print(self, mock):
        rectangle = Rectangle(10, 3, 1, 1, 1)
        print(rectangle)
        excepted_value = mock.getvalue()
        self.assertEqual("[Rectangle] (1) 1/1 - 10/3\n", excepted_value)
    
    def test_update_list(self):
        rectangle = Rectangle(10, 3, 1, 1)

        rectangle.update(20)
        self.assertAlmostEqual(rectangle.id, 20)

        rectangle.update(20, 20)
        self.assertAlmostEqual(rectangle.width, 20)

        rectangle.update(20, 20, 20)
        self.assertAlmostEqual(rectangle.height, 20)

        rectangle.update(20, 20, 20, 20)
        self.assertAlmostEqual(rectangle.x, 20)

        rectangle.update(20, 20, 20, 20, 20)
        self.assertAlmostEqual(rectangle.y, 20)

    def test_update_dict(self):
        rectangle = Rectangle(10, 3, 1, 1)

        rectangle.update(height=20)
        self.assertAlmostEqual(rectangle.height, 20)

        rectangle.update(height=20, width=200)
        self.assertAlmostEqual(rectangle.width, 200)

        rectangle.update(height=20, width=200, id = 200)
        self.assertAlmostEqual(rectangle.id, 200)

        rectangle.update(height=20, width=200, id = 200, x = 2)
        self.assertAlmostEqual(rectangle.x, 2)

        rectangle.update(height=20, width=200, id = 200, x = 2, y = 1)
        self.assertAlmostEqual(rectangle.y, 1)
    
    def test_to_dictionary(self):
        rectangle = Rectangle(10, 2, 1, 9, 12)
        self.assertEqual(json.dumps(rectangle.to_dictionary()), '{"id": 12, "width": 10, "height": 2, "x": 1, "y": 9}')
        rectangle = Rectangle(12, 12, 12, 12, 12)
        self.assertEqual(json.dumps(rectangle.to_dictionary()), '{"id": 12, "width": 12, "height": 12, "x": 12, "y": 12}')

