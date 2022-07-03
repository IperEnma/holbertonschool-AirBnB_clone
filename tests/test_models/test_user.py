#!/usr/bin/python3
"""
testing class User
"""

import unittest
from models import user
from datetime import datetime
from models.user import User


class test_class_base(unittest.TestCase):
    """class for testing class User"""

    @classmethod
    def setUpClass(self):
        """set class"""
        self.my_model = User()

    def setUp(self):
        """ set attr """
        self.dict = self.my_model.to_dict()

    def test_docmodule(self):
        """checking doc module"""
        self.assertGreater(len(user.__doc__), 1)

    def test_docclass(self):
        """checking doc class"""
        self.assertGreater(len(User.__doc__), 1)

    def test_create_base(self):
        """test instance class"""
        self.assertIsInstance(self.my_model, User)

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
        self.kwargs = User(self.dict)
        self.assertIsInstance(self.kwargs, User)

    def test_update(self):
        """ test update date """
        update_old = self.my_model.updated_at
        self.my_model.save()
        update_new = self.my_model.updated_at
        self.assertTrue(update_old != update_new)
