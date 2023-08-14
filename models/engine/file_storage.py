#!/usr/bin/python3
"""file_storage class Module"""
import os
import json


class FileStorage:
    """FileStorage class for storing and retrieving data
     Args:
        __file_path: The string - path to the JSON file (ex: file.json)
        __objects: The dictionary - empty, but will store all objects
                   by <class name>.id
                   (ex: to store a BaseModel object with id=1212121
                   the key will be BaseModel.12121212)
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets the __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the
            JSON file (path: __file_path)
        """
        _dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""

        from models.base_model import BaseModel
        from models.user import User
        from models.review import Review
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity

        objs = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
            }

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                _dict = json.load(f)
            for v in _dict.values():
                self.new(objs[v['__class__']](**v))
