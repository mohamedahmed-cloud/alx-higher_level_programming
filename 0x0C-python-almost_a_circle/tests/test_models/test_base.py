import unittest

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