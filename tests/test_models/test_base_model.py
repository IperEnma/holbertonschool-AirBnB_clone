#!/usr/bin/python3
"""
testing class base
"""

import unittest
from datetime import datetime
from models import base_model
from models.base_model import BaseModel

class test_class_base(unittest.TestCase):
    """class for testing class base model"""
    
    @classmethod
    def setUpClass(self):
        """set class"""
        self.my_model = BaseModel()
    
    def setUp(self):
        """ set attr """
        self.dict = self.my_model.to_dict()

    def test_docmodule(self):
        """checking doc module"""
        self.assertGreater(len(base_model.__doc__), 1)

    def test_docclass(self):
        """checking doc class"""
        self.assertGreater(len(BaseModel.__doc__), 1)

    def test_create_base(self):
        """test instance class BaseModel"""
        self.assertIsInstance(self.my_model, BaseModel)

    def test_attr(self):
        """test attributes"""
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)
        self.assertEqual(type(self.my_model.updated_at), datetime)

        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.assertIn("name", self.my_model.to_dict())
        self.assertIn("my_number", self.my_model.to_dict())
        self.dict = self.my_model.to_dict()
        self.assertEqual(self.dict["my_number"], 89)
        self.assertEqual(self.dict["name"], "My First Model")

    def test_create_kwargs(self):
        """ create class from dictionary """
        self.kwargs = BaseModel(self.dict)
        self.assertIsInstance(self.kwargs, BaseModel)

