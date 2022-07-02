#!/usr/bin/python3

import cmd
import inspect
from models import base_model
from models.base_model import BaseModel
from models.user import User
<<<<<<< HEAD
=======
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
>>>>>>> ema
from models import storage

class HBNBCommand(cmd.Cmd):
    """intrepeter module"""

    prompt = "(hbnt) "
    
    def emptyline(self):
        return ""

    def default(self, line):
        self.stdout.write('[-] Unknown command: %s\n' % (line,))

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """ Quit command to exit the program """
        return True

    def precmd(self, args):
        if (args[-6:] == ".all()"):
            args = "all " + args[:-6]
        if (args[-8:] == ".count()"):
            args = "count " + args[:-8]
        if (args.find(".show(") != -1):
            args = "show " + ((args.replace(".show(", " "))[:-1])
            args = args.replace('"', "")
        if (args.find(".destroy(") != -1):
            args = "destroy " + ((args.replace(".destroy(", " "))[:-1])
            args = args.replace('"', "")
        if (args.find(".update(") != -1):
            if (args.find("{") == -1):
                """ si no me pasan un dict """
                args = "update " + ((args.replace(".update(", " "))[:-1])
                args = args.replace(",", "")
                args = args.replace('"', "")
            else:
                """ si me pasan un dict """
                idx = args.find("{")
                dic = (args[idx:-1])
                args = "update " + args[:idx]
                args = args.replace(".update(", " ")
                args = args.replace(",", "")
                args = args.replace('"', "")
                args = args + dic
        return args

    def do_create(self, args):
        """ Creates a new instance of BaseModel """
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            new_class = eval(args)()
            new_class.save()
            print(new_class.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of an instance """
        if len(args) == 0:
            print("** class name missing **")
            return
        tokens = args.split()
<<<<<<< HEAD
        try:
            eval(tokens[0])()
        except Exception as f:
=======
        
        if tokens[0] not in storage.all_class():
>>>>>>> ema
            print("** class doesn't exist **")

        if len(tokens) < 2:
            print("** instance id missing **")
            return
        key = str(tokens[0]) + '.' + str(tokens[1])
        objects = storage.all()

        try:
            print(objects[key])
        except Exception:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name """
        if len(args) == 0:
            print("** class name missing **")
            return
        tokens = args.split()
        
        if tokens[0] not in storage.all_class():
            print("** class doesn't exist **")
            return

        if len(tokens) < 2:
            print("** instance id missing **")
            return
        key = str(tokens[0]) + '.' + str(tokens[1])
        objects = storage.all()

        if key in objects:
            storage.delete(key) 
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation """
<<<<<<< HEAD
        objects = storage.all()
        tokens = args.split()
        
        if len(tokens) == 1:
=======
        tokens = args.split()
        objects = storage.all()

        if len(tokens) > 0:
            if tokens[0] not in storage.all_class():   
                print("** class doesn't exist **")
                return
            my_list = []
>>>>>>> ema
            for key, value in objects.items():
                if tokens[0] == value.__class__.__name__:
                    print(value)
        else:
             for key, value in objects.items():
                 print(value)

    def do_count(elf, args):
        tokens = args.split()
        objects = storage.all()
        if len(tokens) == 1:
            if tokens[0] not in storage.all_class():
                print("** class doesn't exist **")
            else:
                count = 0
                for k, v in objects.items():
                    if (v.__class__.__name__ == tokens[0]):
                        count += 1
                print(count)

    def do_update(self, args):
        """ Updates an instance based on the class name   """
        if len(args) == 0:
            print("** class name missing **")
            return
        tokens = args.split()
        if tokens[0] not in storage.all_class():
            print("** class doesn't exist **")
            return
        if len(tokens) == 1:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = tokens[0] + "." + tokens[1]
        try:
            obj = objects[key]
        except Exception:
            print("** no instance found **")
            return
        if len(tokens) == 2:
            print("** attribute name missing **")
            return
<<<<<<< HEAD
        if len(tokens) == 3:
            print("** value missing **")
            return
        setattr(obj, tokens[2], (tokens[3])[1:-1])
        """ [1:-1] para quitarle las comillas al value """
=======
        if tokens[2].find("{") == -1:
            if len(tokens) < 4:
                print("** value missing **")
                return

            if tokens[3][0] == '"':
                tokens[3] = tokens[3][1:]
            if tokens[3][-1] == '"':
                tokens[3] = tokens[3][:-1]
            setattr(objects[key], tokens[2], tokens[3])
        else:
            """ update w/ dictionary """
            l = len(tokens);
            dic = ""
            """ todos los tokens menos clase y id """
            for i in range(2, l):
                dic += tokens[i]
            """dic = eval(tokens[2])"""
            dic = eval(dic)
            storage.set_atr(key, dic)
>>>>>>> ema


if __name__ == '__main__':
    HBNBCommand().cmdloop()
