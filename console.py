#!/usr/bin/python3
"""Module defines custom command line interpreter HBNB"""
from models.base_model import BaseModel
import models
import cmd

MODEL_CLASSES = {'BaseModel': BaseModel}


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
