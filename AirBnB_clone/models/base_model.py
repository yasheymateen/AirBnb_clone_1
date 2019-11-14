#!/usr/bin/python3
"""base_model module"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """intiialize"""

        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k in ['created_at', 'updated_at']:
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                self.__setattr__(k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string representation"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """update updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return dictionary representation"""

        original_dict = self.__dict__.copy()
        original_dict['__class__'] = self.__class__.__name__
        original_dict['updated_at'] = self.updated_at.isoformat()
        original_dict['created_at'] = self.created_at.isoformat()

        return original_dict
