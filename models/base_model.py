#!/usr/bin/python3
"""Module that """

import uuid
from datetime import datetime

class BaseModel:
    """create the BaseModel"""

    def __init__(self, *args, **kwargs):
        """ Constructor of BaseModel wich initialices attribute values """
        from models import storage
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, date_format)
                elif key == 'id':
                    self.id = value
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value, date_format)
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Sepcial emthod wich returns in a string class, id, and object inf"""
        str_f = "[{}] ({}) {}"
        return str_f.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute with the current datetime """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance """
        dictionary = self.__dict__.copy()
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['__class__'] = self.__class__.__name__
        return dictionary
