#!/usr/bin/python3
"""
test module file storage
"""

import unittest
from models.engine import file_storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_file_storage(unittest.TestCase):
    """ class test file storage """

    @classmethod
    def setUpClass(self):
        """ set instance class """
        self.my_model = BaseModel()
        self.storage = FileStorage()

    def test_docmodule(self):
        """ checking doc module """
        self.assertGreater(len(file_storage.__doc__), 1)

    def test_docclass(self):
        """checking doc class"""
        self.assertGreater(len(BaseModel.__doc__), 1)

    def test_create_FileStorage(self):
        """test instance class FileStorage"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_reload(self):
        """ test reload from json """
        self.my_model.name = "My_first_model"
        self.my_model.my_number = 89
        self.my_model.save()
        self.storage.reload()
        objs = self.storage.all()
        for obj_id in objs.keys():
            obj_reload = objs[obj_id]
        self.assertTrue(self.my_model.__dict__ == obj_reload.__dict__)
        self.assertTrue(self.my_model is not obj_reload)
