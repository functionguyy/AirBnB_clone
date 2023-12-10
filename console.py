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
        arg_list, arg_count = self.parse_cmd(cmd_arg)

        output_list = []
        objs_dict = models.storage.all()
        if arg_count == 0:
            for key, value in objs_dict.items():
                output_list.append(str(value))
        elif arg_count > 0:
            for key in objs_dict.keys():
                cls_name, id_ = key.split('.')
                if cls_name == arg_list[0]:
                    value = str(objs_dict[key])
                    output_list.append(value)

        if len(output_list) > 0:
            print(output_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, cmd_arg):
        """updates an instance based on the class name and id by adding or
        updating attribute
        """
        arg_list, arg_count = self.parse_cmd(cmd_arg)

        match arg_count:
            case 0:
                print("** class name missing **")
            case 1:
                if arg_list[0] not in self.model_classes.keys():
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            case 2:
                print("** attribute name missing **")
            case 3:
                print("** value missing **")
            case _:
                storage_key = f"{arg_list[0]}.{arg_list[1]}"
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
                    model_inst.save()
                except KeyError:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
