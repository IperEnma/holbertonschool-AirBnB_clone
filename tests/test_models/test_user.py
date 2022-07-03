#!/usr/bin/python3
"""
testing class base
"""

import unittest
from datetime import datetime
from models import user
from models.user import User

class test_class_base(unittest.TestCase):
    """class for testing class base model"""
    
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

    def test_all(self):
        """test instance class BaseModel"""
        self.assertIsInstance(self.my_model, User)
        u = self.my_model



