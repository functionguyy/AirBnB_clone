#!/usr/bin/python3
"""Module defines custom command line interpreter HBNB"""
from models.base_model import BaseModel
import models
import cmd

MODEL_CLASSES = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """define internals of a HBNBCommand instance"""

    prompt = "(hbnb) "

    model_classes = MODEL_CLASSES

    def do_create(self, cmd_arg):
        """
        create a new instance of BaseModel, saves it to JSON file and prints
        the id
        """
        if cmd_arg in self.model_classes.keys():
            model_cls = self.model_classes[cmd_arg]
            new_model = model_cls()
            print("{:s}".format(new_model.id))
            models.storage.save()
        elif cmd_arg == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, cmd_arg):
        """
        prints the string representation of an instance based on the class
        name and id
        """
        flag, objs_dict, storage_key = self.check_arg(cmd_arg)

        if flag:
            try:
                found = objs_dict[storage_key]
                print("{}".format(found))
            except KeyError:
                print("** no instance found **")

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
