#!/usr/bin/python3
"""
test module file storage
"""

import unittest
from models.base_model import BaseModel
from models import storage


class test_file_storage(unittest.TestCase):
    """ class test file storage """

    def test_reload(self):
        """ test reload from .json """
        self.my_model = BaseModel()
        self.my_model.save()
        storage.reload()
        objs = storage.all()
        for obj_id in objs.keys():
            obj_reload = objs[obj_id]
        self.assertTrue(self.my_model.__dict__ == obj_reload.__dict__)

    def test_newattr(self):
        """ test add new attr """
        self.my_model = BaseModel()
        self.my_model.name = "My_first_model"
        self.my_model.my_number = 89
        self.my_model.save()
        storage.reload()
        objs = storage.all()
        for obj_id in objs.keys():
            obj_reload = objs[obj_id]
        self.assertTrue(self.my_model.__dict__ == obj_reload.__dict__)
