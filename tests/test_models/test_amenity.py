#!/usr/bin/python3
"""Test Module that contain the test of class amenity"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test class Amenity"""

    def setUp(self):
        self.new_amenity = Amenity()

    def test_amenity(self):
        self.assertIsInstance(self.new_amenity, Amenity)
        self.assertEqual(type(self.new_amenity.name), str)
        self.assertEqual(self.new_amenity.name, "")
