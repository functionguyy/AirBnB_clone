#!/usr/bin/python3
"""Module defines class Base"""
import uuid
from datetime import datetime, timezone


class BaseModel:
    """Defines the internals of a BaseModel object"""

    def __init__(self):
        """Initialize an instance of a BaseModel object type"""
        current_datetime = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = current_datetime
        self.updated_at = current_datetime


    def __str__(self):
        """print string representation of instance"""
        id_ = self.id
        class_name = type(self).__name__
        attr_dict = self.__dict__

        return "[{:s}] ({:s}) {}".format(class_name, id_, attr_dict)


    def save(self):
        """update the public instance attribute updated_at with current
        datetime"""
        self.updated_at = datetime.now()


    def to_dict(self):
        """returns a dictionary containing all key/values of __dict__ of the
        instance"""
        instance_attr = self.__dict__
        instance_attr['__class__'] = type(self).__name__

        # keys with datetime object values
        change_keys = ['updated_at', 'created_at']

        # convert datetime object values to isoformat string
        for k in instance_attr.keys():
            if k in change_keys:
                new_value = instance_attr[k].isoformat() # convert to isoformat
                instance_attr[k] = new_value

        return instance_attr
