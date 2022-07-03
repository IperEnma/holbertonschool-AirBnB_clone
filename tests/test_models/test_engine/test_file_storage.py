#!/usr/bin/python3
"""
test module file storage
"""

import pep8
import json
import unittest
import os
from os import remove
from models import base_model
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class test_file_storage(unittest.TestCase):
    """ class test file storage """

    def setUp(self):
        """ set instance class """
        self.my_model = BaseModel()
        self.storage = file_storage.FileStorage()

    def test_docmodule(self):
        """ checking doc module """
        self.assertIsNotNone(file_storage.__doc__)

    def test_docclass(self):
        """checking doc class"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_json(self):
        """Check file json"""
        with open("file.json") as f:
            self.assertGreater(len(f.read()), 0)

    def test_reload(self):
        """ test reload from json """
        self.my_model.name = "My_first_model"
        self.my_model.my_number = 89
        name = str(self.my_model.__class__.__name__)
        key = name + "." + str(self.my_model.id)
        self.my_model.save()
        self.storage.reload()
        objs = self.storage.all()
        self.assertIsNotNone(objs[key])
        self.obj_reload = objs[key]
        self.assertTrue(self.my_model.__dict__ == self.obj_reload.__dict__)
        self.assertTrue(self.my_model is not self.obj_reload)
        self.assertIsInstance(self.obj_reload, BaseModel)
        self.assertTrue(self.storage.all(), "My_first_model")

    def test_inst(self):
        """ test instance """
        i = FileStorage()
        self.assertEqual(i.path(), "file.json")
        bm = BaseModel()
        i.new(bm)
        self.assertGreater(len(i.all()), 0)

        """agrego basemodel test"""

    @classmethod
    def setUpClass(self):
        """set class"""
        self.my_model = BaseModel()

    def setUp(self):
        """ set attr """
        self.dict = self.my_model.to_dict()

    def test_docmodule(self):
        """checking doc module"""
        self.assertIsNotNone(base_model.__doc__)

    def test_docclass(self):
        """checking doc class"""
        self.assertIsNotNone(BaseModel.__doc__)

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

    def test_update(self):
        """ test update date """
        update_old = self.my_model.updated_at
        self.my_model.save()
        update_new = self.my_model.updated_at
        self.assertTrue(update_old != update_new)
