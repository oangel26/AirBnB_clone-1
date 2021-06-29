#!/usr/bin/python3
"""Module that declare class city"""

from models.state import State
from models.base_model import BaseModel


class City(BaseModel):
    """Class City"""
    state_id = ""
    name = ""
