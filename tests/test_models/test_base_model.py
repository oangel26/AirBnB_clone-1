#!/usr/bin/python3

from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.my_model = BaseModel()

    def test_base_model(self):
        self.my_model.name = ""
        self.my_model.my_number = 89
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertEqual(self.my_model.name, "")
        self.assertEqual(type(self.my_model.name), str)
        self.assertEqual(type(self.my_model.my_number), int)
        self.assertEqual(self.my_model.my_number, 89)
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)
        self.assertEqual(type(self.my_model.updated_at), datetime)
"""
    def test_base_model_kwargs(self):
        attributes = {'id': "565741c1-f2f9-4bd4-8b66-b73ffe1e3d45",
        'created_at': '2021-06-28T21:10:25.934419',
        'updated_at': '2021-06-28T21:10:33.702066',
        'first_name': 'Betty',
        "last_name": "Holberton",
        "email": "airbnb@holbertonshool.com",
        "password": "root"}
        my_model = BaseModel(**attributes)
        self.assertEqual(my_model.id, "565741c1-f2f9-4bd4-8b66-b73ffe1e3d45")
        self.assertEqual(my_model.updated_at, "2021-06-28T21:10:33.702066")
        self.assertEqual(my_model.created_at, "2021-06-28T21:10:25.934419")
        self.assertEqual(my_model.first_name, "Betty")
        self.assertEqual(my_model.last_name, "Holberton")
        self.assertEqual(my_model.email, "airbnb@holbertonshool.com")
        self.assertEqual(my_model.password, "root")"""
