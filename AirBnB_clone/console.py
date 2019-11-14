#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from datetime import datetime
from shlex import shlex

""" hbnb console """


class HBNBCommand(cmd.Cmd):
    """ hbnb shell """
    prompt = '(hbnb) '
    list_of_classes = {'BaseModel': BaseModel, 'State': State, 'City': City,
                       'Amenity': Amenity, 'Place': Place, 'Review': Review,
                       'User': User}

    def emptyline(self):
        """ empty line """
        pass

    def do_create(self, class_name=None):
        """creates a new instance of BaseModel"""
        if not class_name:
            print("** class name missing **")
        elif not self.list_of_classes.get(class_name):
            print("** class doesn't exist **")
        else:
            obj = self.list_of_classes[class_name]()
            models.storage.save()
            print(obj.id)

    def do_show(self, argument):
        """prints string representation of an instance"""
        class_name, obj_id = None, None

        args = argument.split(' ')
        if len(args) > 0:
            class_name = args[0]
        if len(args) > 1:
            obj_id = args[1]

        if not class_name:
            print("** class name missing **")

        elif not obj_id:
            print("** instance id missing **")

        elif not self.list_of_classes.get(class_name):
            print("** class doesn't exist **")
        else:
            k = class_name + "." + obj_id
            obj = models.storage.all().get(k)

            if not obj:
                print("** no instance found **")

            else:
                print(obj)

    def do_destroy(self, argument):
        """destroy instance from the id"""
        class_name, obj_id = None, None
        args = argument.split(' ')
        if len(args) > 0:
            class_name = args[0]
        if len(args) > 1:
            obj_id = args[1]

        if not class_name:
            print("** class name missing **")

        elif not obj_id:
            print("** instance id missing **")

        elif not self.list_of_classes.get(class_name):
            print("** class doesn't exist **")
        else:
            k = class_name + "." + obj_id
            obj = models.storage.all().get(k)

            if not obj:
                print("** no instance found **")

            else:
                del models.storage.all()[k]
                models.storage.save()

    def do_all(self, argument):
        """ prints all instances """
        if not argument:
            for k, v in models.storage.all().items():
                print(str(v))

        else:
            if not self.list_of_classes.get(argument):
                print("** class doesn't exist **")
                return False
            for k, v in models.storage.all().items():
                if type(v) is self.list_of_classes.get(argument):
                    print(str(v))

    def do_update(self, argument):
        """ updates an instance"""
        class_name, obj_id, attr_k, attr_v = None, None, None, None

        args = argument.split(' ', 3)
        if len(args) > 0:
            class_name = args[0]
        if len(args) > 1:
            obj_id = args[1]
        if len(args) > 2:
            attr_k = args[2]
        if len(args) > 3:
            attr_v = list(shlex(args[3]))[0].strip('"')
        if not class_name:
            print("** class name missing **")
        elif not obj_id:
            print("** instance id missing **")
        elif not attr_k:
            print("** attribute name missing **")
        elif not attr_v:
            print("** value missing **")
        elif not self.list_of_classes.get(class_name):
            print("** class doesn't exist **")
        else:
            k = class_name + "." + obj_id
            obj = models.storage.all().get(k)

            if not obj:
                print("** no instance found **")

            else:
                if hasattr(obj, attr_k):
                    attr_v = type(getattr(obj, attr_k))(attr_v)
                else:
                    attr_v = self.input_type(attr_v)(attr_v)

                setattr(obj, attr_k, attr_v)
                obj.updated_at = datetime.now()
                models.storage.save()

    def do_quit(self, argument):
        """Quit command to exit program"""
        return True

    def do_EOF(self, argument):
        """EOF signal to exit program"""
        return True

    def default(self, inputs):
        """deal with commands """
        i = inputs.split('.', 1)
        if len(i) < 2:
            print('*** Unknown syntax:', i[0])
            return False

        class_name, inputs = i[0], i[1]

        if class_name not in list(self.list_of_classes.keys()):
            print('*** Unknown syntax: {}.{}'.format(class_name, inputs))
            return False

        i = inputs.split('(', 1)
        if len(i) < 2:
            print('*** Unknown syntax: {}.{}'.format(class_name, i[0]))
            return False

        method_name, argument = i[0], i[1].rstrip(')')

        if method_name not in ['all', 'show', 'destroy', 'update', 'count']:
            print('*** Unknown syntax: {}.{}'.format(class_name, inputs))
            return False

        if method_name == 'all':
            self.do_all(class_name)

        elif method_name == 'count':
            print(self.count_class(class_name))

        elif method_name == 'show':
            self.do_show(class_name + " " + argument.strip('"'))

        elif method_name == 'destroy':
            self.do_destroy(class_name + " " + argument.strip('"'))

        elif method_name == 'update':
            l_bracket_search = argument.find('{')
            r_bracket_search = argument.find('}')
            dic = None

            if argument[l_bracket_search:r_bracket_search + 1] != '':
                dic = eval(argument[l_bracket_search:r_bracket_search + 1])

            i = argument.split(',', 1)
            obj_id = i[0].strip('"')
            argument = i[1]

            if dic and type(dic) is dict:
                self.dictionary_update(obj_id, class_name, dic)

            else:
                argument = argument.replace(',', ' ', 1)
                i = list(shlex(argument))
                i[0] = i[0].strip('"')

                self.do_update(" ".join([class_name, obj_id, i[0], i[1]]))

    def dictionary_update(self, obj_id, class_name, dic):
        """ update dictionary """
        for k, v in dic.items():
            self.do_update(" ".join([class_name, obj_id, str(k), str(v)]))

    @staticmethod
    def count_class(class_name):
        """ counts the number of type class_name """
        c = 0
        for k, v, in models.storage.all().items():
            if type(v).__name__ == class_name:
                c += 1
        return (c)

    @staticmethod
    def input_type(attr_v):
        """ retrieves the input type """
        try:
            int(attr_v)
            return (int)
        except ValueError:
            pass
        try:
            float(attr_v)
            return float
        except ValueError:
            return (str)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
