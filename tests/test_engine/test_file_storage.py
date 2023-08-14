#!/usr/bin/python3
"""unittest module for file_storage class."""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):
    """Test case for file_storage class"""

    @classmethod
    def setUpClass(cls):
        """test for set up"""
        cls.file_path = "test_file.json"
        cls.storage = FileStorage()
        cls.storage._FileStorage__file_path = cls.file_path

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)

    def setUp(self):
        """set up"""

        self.storage._FileStorage__objects = {}

    def test_save(self):
        """test save method"""
        B_m = BaseModel()
        self.storage.new(B_m)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_new(self):
        """test new method"""
        B_m = BaseModel()
        self.storage.new(B_m)
        objects = self.storage.all()
        key = f"{B_m.__class__.__name__}.{B_m.id}"
        self.assertIn(key, objects)

    def test_all(self):
        """test all method"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_reload_creates_objects(self):
        """test reload method for created objects"""
        B_m = BaseModel()
        user = User()
        self.storage.new(B_m)
        self.storage.new(user)
        self.storage.save()
        New__Storage = FileStorage()
        New__Storage._FileStorage__file_path = self.file_path
        New__Storage.reload()
        objects = New__Storage.all()
        Key_BM = f"{B_m.__class__.__name__}.{B_m.id}"
        user_key = f"{user.__class__.__name__}.{user.id}"
        self.assertIsInstance(objects[Key_BM], BaseModel)
        self.assertIsInstance(objects[user_key], User)

    def test_reload(self):
        """test reload method"""
        B_m = BaseModel()
        self.storage.new(B_m)
        self.storage.save()
        New__Storage = FileStorage()
        New__Storage._FileStorage__file_path = self.file_path
        New__Storage.reload()
        objects = New__Storage.all()
        key = f"{B_m.__class__.__name__}.{B_m.id}"
        self.assertIn(key, objects)


if __name__ == "__main__":
    unittest.main()
