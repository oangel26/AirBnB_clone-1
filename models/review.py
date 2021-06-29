#!/usr/bin/python3
"""class review"""

from models.base_model import BaseModel
from models.place import Place
from models.user import User

class Review(BaseModel):
    """ Class wich describes data type of Rivew and inherits from
    BaseModel """
    place_id = ""
    user_id = ""
    text = ""
