#!/usr/bin/python3
"""Module defines custom command line interpreter HBNB"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """define internals of a HBNBCommand instance"""

    prompt = "(hbnb) "

    def do_quit(self, cmd_arg):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, cmd_arg):
        print()
        return True

    def help_EOF(self):
        print("Exit the interpreter")
        print("You can also use the ctrl-D shortcut.")

    def emptyline(self):
        pass

    def do_create(self, cmd_arg):
        """creates a new instance of BaseModel, saves it to JSON file and
        prints the id
        """
        if cmd_arg == "BaseModel":
            new_model = BaseModel()
            new_model.save()
            print("{:s}".format(new_model.id))
        elif cmd_arg == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
