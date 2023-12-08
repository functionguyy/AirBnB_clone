#!/usr/bin/python3
"""Module defines class FileStorage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Defines the internals of a FileStorage object"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects which stores all objects by <class
        name>.id"""
        return type(self).__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_cls_name = type(obj).__name__
        obj_id = obj.id

        key_members = [obj_cls_name, obj_id]
        storage_key = ".".join(key_members)

        type(self).__objects[storage_key] = obj

    def save(self):
        """serializes __objects to the JSON file __file_path"""
        objs = type(self).__objects
        obj_dict = {key: obj.to_dict() for key, obj in objs.items()}

        filename = type(self).__file_path
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if JSON file
        __file_path exists; otherwise, do nothing. If the file doesn't exist,
        no exception is raised
        """
        filep = type(self).__file_path

        try:
            with open(filep, "r", encoding="utf-8") as f:
                models_dict = json.load(f)
                for key, obj in models_dict.items():
                    obj_cls = obj['__class__']
                    type(self).__objects[key] = BaseModel(**obj)
        except FileNotFoundError:
            pass
