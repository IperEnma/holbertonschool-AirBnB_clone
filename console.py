#!/usr/bin/python3

import cmd
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
        return True

    def do_EOF(self):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("exit the program")

    def do_create(self, args):
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            new_class = eval(args)()
            new_class.save()
        except Exception as f:
            print("** class doesn't exist **")

    def do_show(self, args):
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

        if objects[key]:
            storage.delete(key) 
            storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
