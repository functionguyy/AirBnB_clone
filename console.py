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

    def check_arg(self, cmd_arg):
        """ parse command arguments"""

        arg_list, arg_count = self.parse_cmd(cmd_arg)
        flag, objs_dict, storage_key = False, None, None

        match arg_count:
            case 0:
                print("** class name missing **")
            case 1:
                if arg_list[0] not in self.model_classes.keys():
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            case _:
                storage_key = f"{arg_list[0]}.{arg_list[1]}"
                objs_dict = models.storage.all()
                flag = True

        return flag, objs_dict, storage_key

    def do_show(self, cmd_arg):
        """prints the string representation of an instance based on the class
        name and id
        """
        flag, objs_dict, storage_key = self.check_arg(cmd_arg)

        if flag:
            try:
                found = objs_dict[storage_key]
                print(found)
            except KeyError:
                print("** no instance found **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
