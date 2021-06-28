#!/usr/bin/python3
"""Class city"""

from models.state import State
from models.base_model import BaseModel

class City(BaseModel):
    state_id = ""
    name = ""