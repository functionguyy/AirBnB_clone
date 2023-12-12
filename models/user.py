#!/usr/bin/python3
"""Module defines class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines the internals of a User object"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
