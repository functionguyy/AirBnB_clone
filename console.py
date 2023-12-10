#!/usr/bin/python3
"""Module defines custom command line interpreter HBNB"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """define internals of a HBNBCommand instance"""

    prompt = "(hbnb) "
    model_classes = {'BaseModel': BaseModel}

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
        """
        creates a new instance of BaseModel, saves it to JSON file and
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

    def check_arg(self, cmd_arg):
        """ parse command arguments"""

        arg_members = cmd_arg.split()
        arg_count = len(arg_members)
        flag, objs_dict, storage_key = False, None, None

        match arg_count:
            case 0:
                print("** class name missing **")
            case 1:
                if arg_members[0] not in self.model_classes.keys():
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            case _:
                storage_key = '.'.join(arg_members)
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
                print("{}".format(found))
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, cmd_arg):
        """deletes an instance based on the class name and id"""
        flag, objs_dict, storage_key = self.check_arg(cmd_arg)

        if flag:
            try:
                del objs_dict[storage_key]
                models.storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, cmd_arg):
        """prints all string representation of all instances based or not on
        the class name
        """
        if cmd_arg not in self.model_classes.keys():
            print("** class doesn't exist **")
        else:
            output_list = []
            objs_dict = models.storage.all()
            for key in objs_dict.keys():
                cls_name, id_ = key.split('.')
                if cls_name == cmd_arg:
                    output_list.append(str(objs_dict[key]))
            print(output_list)

    def do_update(self, cmd_arg):
        """updates an instance based on the class name and id by adding or
        updating attribute
        """
        arg_members = cmd_arg.split()
        arg_count = len(arg_members)

        match arg_count:
            case 0:
                print("** class name missing **")
            case 1:
                if arg_members[0] not in self.model_classes.keys():
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            case 2:
                print("** attribute name missing **")
            case 3:
                print("** value missing **")
            case _:
                import re
                storage_key = arg_members[0] + '.' + arg_members[1]
                objs_dict = models.storage.all()
                try:
                    model_inst = objs_dict[storage_key]
                    inst_attr = model_inst.__dict__
                    attr_key = arg_members[2]
                    attr_value = arg_members[3].strip("\"'")

                    if attr_key in inst_attr.keys():
                        attr_type = type(inst_attr[attr_key])
                        attr_value = attr_type(attr_value)
                    setattr(model_inst, attr_key, attr_value)
                except KeyError:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
