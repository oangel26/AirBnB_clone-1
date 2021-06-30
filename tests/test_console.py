#!/usr/bin/python3
"""Test Module that contain the test of class amenity"""


import unittest
from models.engine.file_storage import FileStorage


class Testconsole(unittest,TestCase):
    """test class Amenity"""

    def setUp(self):
        """create a instance"""
        self.new_file_storage = FileStorage()