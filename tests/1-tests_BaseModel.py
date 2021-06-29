#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class that check a differents cases of success and failures
    with a different test, with de unittest
    """

    def test_max_inlist(self):
        """Function that check a cases with a different integers, float,
        and only number inside of the list
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2.3, 5.4, -1]), 5.4)
        self.assertEqual(max_integer([1, 2, -3, -4]), 2)
        self.assertEqual(max_integer([1]), 1)