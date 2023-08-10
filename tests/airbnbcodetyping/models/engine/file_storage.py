#!/usr/bin/env python3
"""FileStorage class

This modules has clas that serializes objects to JSON files
and vice versa
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """sets the blueprints of saving and retrieving objecsts

    Attributes:
        __file_path: string - pathe to the json format file.
        __objects: string - empty as the start but should store some <class.name>.id
    """
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """returns all objects created"""
        return FileStorage.objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        cl_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj
    def save(self, obj):
        """Serializes objects to json file"""
        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes jsonfile to odjects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                object_load = json.load(f)

                new_dict = {}
                for key, dict_object in object_load.items():
                    cl_name = key.split(".")[0]
                    obj = eval(cl_name)(**dict_object)
                    new_dict[key] = obj
                FileStorage.__objects = new_dict
        except FileNotFoundError:
            pass
    def delete(self, obj):
        """deletes objects from the file json"""
        cl_name = type(obj).__name__
        object_id = obj.id
        key = f"{cl_name}.{object_id}"

        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
            self.save()
            return True

        return False
