#!/usr/bin/python3
"""Module defines class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines the internals of a City object"""
    state_id = ""
    name = ""
