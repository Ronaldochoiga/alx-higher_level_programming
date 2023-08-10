#!/usr/bin/env python3
"""HBNBCommad class

Custom cmd for airbnb project.
"""

import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    """shows models and methods of the console"""

    prompt = ("hbnb")

    models = ("Amenity", "BaseModel", "City", "Place", "Review", "State", "User")
    def do_quit(self, arg):
        """quit command that exits the program"""
        return True

    def do_EOF(self, arg):
        """signals the end of a program through signalling"""
        print("")
        return True

    def emptyline(self, arg):
        """This ignores an empty line thus no execution"""
        return False

    def do_create (self, arg):
        """this creates an instance and saves on json file"""
        arg0 = parse(arg)
        if len(arg0) == 0:
            print("** class name missing **")
        elif arg0[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg0)[0]().id)
            storage.save()
    def do_show(self, arg):
        """prints representation of instance based on id and class"""
        arg0 = parse(arg)
        obdict = storage.all()
        if len(arg0) == 0:
            print("** class name missing **")
        elif arg0[0] not in HBNBCommabd.__classes:
            print("** class doesn't exist **")
        elif len(arg0) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg0[0], arg0[1]) not in obdict:
            print("** no instance found **")
        else:
            print(obdict["{}.{}".format(arg0[0], arg0[1])])
    def do_destroy(self, arg):
        """deletes an instance based on the class name and id"""
        arg0 = parse(arg)
        obdict = storage.all()
        if len(arg0) == 0:
            print("** class name missing **")
        elif arg0[0] not in HBNBCommand.__classes:
            print("** instance id missing **")
        elif len(arg0) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg0[0], arg0[1]) not in obdict.keys():
            print("** no instance found **")
        else:
            del obdict["{}.{}".format(arg0[0], arg0[1])]
            storage.save()
    def do_all(self, args):
        """displays string reprentation of instances of a given class"""
        arg0 = parse(arg)
        if len(arg0) > 0 and arg0[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj0 = []
            for obj in storage.all().values():
                if  len(arg0) > 0 and arg0[0] == obj.__class.__name:
                    obj0.append(obj.__str__())
                elif len(arg0) == 0:
                    obj0.append(obj.__str__())
            print(obj0)

    def do_count(self, arg):
        """this returns the number of the objects within a certain class"""
        arg0 = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg0[0] == obj.__class__.__name__:
                count += 1
            print(count)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file)"""
        arg0 = parse(arg)
        obdict = storage.all()

        if len(arg0) == 0:
            print("** class name missing **")
            return False
        if arg0[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg0) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg0[0], arg0[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(arg0) == 2:
            print("** attribute name missing **")
            return False
        if len(arg0) == 3:
            try:
                type(eval(arg0[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg0) == 4:
            obj = obdict["{}.{}".format(arg0[0], arg0[1])]
            if arg0[2] in obj.__class__.__dict__.keys():
                valuetype = type(obj.__class__.__dict__[arg0[2]])
                obj.__dict__[arg0[2]] = valuetype(arg0[3])
            else:
                obj.__dict__[arg0[2]] = arg0[3]
        elif type(eval(arg0[2])) == dict:
            obj = obdict["{}.{}".format(arg0[0], arg0[1])]
            for key, value in eval(arg0[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    valuetype = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valtype(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
