#!/usr/bin/python3
"""Test Module that contain the test of class review"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test class review"""

    def setUp(self):
        self.new_review = Review()

    def test_review(self):
        self.assertEqual(type(self.new_review.user_id), str)
        self.assertEqual(type(self.new_review.place_id), str)
        self.assertEqual(type(self.new_review.text), str)
