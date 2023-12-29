#!/usr/bin/python3
"""Module defines class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the internals of a review object"""
    place_id = ""
    user_id = ""
    text = ""
