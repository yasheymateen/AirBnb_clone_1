#!/usr/bin/python3
""" Filestorage class"""

import json
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionary objects"""
        return type(self).__objects

    def new(self, obj):
        """ add object to objects """
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[k] = obj

    def save(self):
        """saves the serialized objects into a file"""
        serialized_obj = {}

        for k, v in type(self).__objects.items():
            serialized_obj[k] = v.to_dict()

        with open(type(self).__file_path, "w", encoding='utf-8') as f:
                f.write(json.dumps(serialized_obj) + '\n')

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        exists; otherwise, do nothing """

        classes = {'BaseModel': BaseModel, 'State': State, 'City': City,
                   'Amenity': Amenity, 'Place': Place, 'Review': Review,
                   'User': User}

        try:
            with open(type(self).__file_path, "r", encoding='utf-8') as f:
                txtfile = json.load(f)

                for k, v in txtfile.items():
                    self.new(classes[v['__class__']](**v))

        except FileNotFoundError:
            pass
