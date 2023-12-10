#!/usr/bin/python3
"""Module defines custom command line interpreter HBNB"""
import cmd
from models.base_model import BaseModel
import models

MODEL_CLASSES = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """define internals of a HBNBCommand instance"""

    prompt = "(hbnb) "
    model_classes = MODEL_CLASSES

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

    def parse_cmd(self, cmd_arg):

        arg_list = cmd_arg.split()
        arg_count = len(arg_list)

        return arg_list, arg_count

    def do_create(self, cmd_arg):
        """
        creates a new instance of BaseModel, saves it to JSON file and
        prints the id
        """

        arg_list, arg_count = self.parse_cmd(cmd_arg)

        if arg_count == 0:
            print("** class name missing **")
        elif arg_count > 0:
            try:
                model_cls = self.model_classes[arg_list[0]]
                new_model = model_cls()
                print("{:s}".format(new_model.id))
                models.storage.save()
            except KeyError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
