import unittest
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
    
