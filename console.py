#!/usr/bin/python3

import cmd
import inspect
from models import base_model
from models.base_model import BaseModel
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

    def do_create(self, args):
        """ Creates a new instance of BaseModel """
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            new_class = eval(args)()
            new_class.save()
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of an instance """
        if len(args) == 0:
            print("** class name missing **")
            return
        tokens = args.split()
        try:
            eval(tokens[0])()
        except Exception as f:
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
        
        if globals().get(tokens[0]) is None:
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
        objects = storage.all()
        tokens = args.split()
        
        if len(tokens) == 1:
            for key, value in objects.items():
                if tokens[0] == value.__class__.__name__:
                    print(value)
        else:
             for key, value in objects.items():
                 print(value)
    def do_update(self, args):
        """ Updates an instance based on the class name   """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
