#!/usr/bin/python3
"""
testing class base
"""

import unittest
from models import base_model

class test_class_base(unittest.TestCase):
    """class for testing class base model"""

    def test_base(self):
        """checking doc module"""
        self.assertEqual(1, 1)
