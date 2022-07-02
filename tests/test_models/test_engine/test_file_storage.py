#!/usr/bin/python3
"""
test module file storage
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_file_storage(unittest.TestCase):
    """ class test file storage """

    @classmethod
    def setUpClass(self):
        """ set instance class """
        self.my_model = BaseModel()
        self.storage = FileStorage()

    def test_reload(self):
        """ test reload with new attr """
        self.my_model.name = "My_first_model"
        self.my_model.my_number = 89
        self.my_model.save()
        self.storage.reload()
        objs = self.storage.all()
        for obj_id in objs.keys():
            obj_reload = objs[obj_id]
        self.assertTrue(self.my_model.__dict__ == obj_reload.__dict__)

    def test_file(self):
        """ test file existence """
        self.assertTrue(self.storage.path(), "file.json")
