#!/usr/bin/python3
"""class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Class wich describes User data type and inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
