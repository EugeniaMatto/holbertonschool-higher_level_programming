#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        #Test maxs when list is all 0
        self.assertAlmostEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertAlmostEqual(max_integer([43, 88, 2, 31]), 88)
        self.assertAlmostEqual(max_integer([-66, -77, -54, -70]), -54)
        self.assertRaises(TypeError, max_integer, [0, 0, 0, "Hola"], "")
        self.assertRaises(TypeError, max_integer, "Hola", "")
        self.assertRaises(TypeError, max_integer, 9, "")
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1, 1, 1, 1, 1, 1, 1, 1, -4]), 1)
        self.assertAlmostEqual(max_integer([1, -4, -2 , -3]), 1)
        self.assertAlmostEqual(max_integer([1, 2]), 2)
        self.assertAlmostEqual(max_integer([2, 1]), 2) 


if __name__ == "__main__":
    unittest.main()
