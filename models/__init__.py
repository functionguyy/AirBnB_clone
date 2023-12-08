#!/usr/bin/python3
"""Initialize the models package"""
from models.engine import file_storage

# explicitly import all model class names to make it available for package
# modules
from models.base_model import BaseModel



models_dict = {"BaseModel": BaseModel}
storage = file_storage.FileStorage()
storage.reload()
