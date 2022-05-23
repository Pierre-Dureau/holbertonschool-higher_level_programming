#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test function"""

    def test_max_integer(self):
        """Tests output for the max integer"""

        li = [1, 2, 3, 4]
        self.assertEqual(max_integer(li), 4)
        li = [4, -3, 2, -1]
        self.assertEqual(max_integer(li), 4)
        li = [2, 1, 5, 3, 6, 4, 1, 2]
        self.assertEqual(max_integer(li), 6)
        li = [None]
        self.assertEqual(max_integer(li), None)
        li = []
        self.assertEqual(max_integer(li), None)
        li = [1, 2, 3, float(4)]
        self.assertEqual(max_integer(li), 4)
        li = [1, 4, float(3), 2]
        self.assertEqual(max_integer(li), 4)

    def test_type_integer(self):
        """Tests type for the max integer"""

        li = [1, 3, "Holberton", 2]
        self.assertRaises(TypeError, max_integer, li)
        li = None
        self.assertRaises(TypeError, max_integer, li)


if __name__ == '__main__':
    unittest.main()
