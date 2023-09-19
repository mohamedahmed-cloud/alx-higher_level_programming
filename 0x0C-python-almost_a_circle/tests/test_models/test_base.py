import unittest, json

from models.base import Base
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
