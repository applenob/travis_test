import unittest
from module1 import func1


class Module1Test(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(3, func1(1, 2))
