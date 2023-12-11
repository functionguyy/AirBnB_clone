#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class AllAttrTestCase(unittest.TestCase):


    def test_all_attr_output(self):
        """all should return a dictionary object"""

        a = FileStorage()
        self.assertIs(type(a.all()), dict)

class NewAttributeTestCase(unittest.TestCase):


    def test_new_attr_output(self):
        """new should set in __object obj with key <obj class name>.id"""

        a = FileStorage()

        b = BaseModel()

        key_members = [type(b).__name__, b.id]

        new_key = ".".join(key_members)
        # new_key = type(b).__name__

        a.new(b)
        storage_dict = a._FileStorage__objects
        storage_keys = storage_dict.keys()

        self.assertIn(new_key, storage_keys)

