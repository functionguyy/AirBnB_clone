#!/usr/bin/python3
"""Module defines custom command line interpreter HBNB"""
import cmd
from models.engine.file_storage import FileStorage
import models
import re


class HBNBCommand(cmd.Cmd):
    """define internals of a HBNBCommand instance"""

    prompt = "(hbnb) "
    # model_classes = MODEL_CLASSES

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

    def precmd(self, line):
        """Hook method executed just before the command line is interpreted,
        but after the input prompt is generated and issued."""

        # Add regex to check if line matches string.string() and then split
        # on the period else return line just as is
        m = re.match(r'([A-Za-z]+\.[a-z]+)[(](.*)[)]', line)

        if m:
            line_str = m.group(1)
            arg = m.group(2)
            model_cls, cmd = line_str.split(".")
            line = cmd + " " + model_cls
            if len(arg) != 0:
                arg_list = re.split('\s+', arg)
                if len(arg_list) == 1:
                    arg = arg_list[0].strip('"\'')
                else:
                    new_list = []
                    for item in arg_list:
                        new_ = item.strip('"\',')
                        new_list.append(new_)
                    arg = ' '.join(new_list)
                line = line + " " + arg

        return line

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
                model_cls = FileStorage.model_classes[arg_list[0]]
                new_model = model_cls()
                print(new_model.id)
                models.storage.save()
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, cmd_arg):
        """
        Prints the string representation of an instance based on the class name
        and id.

        example: $ show BaseModel 121212

        """

        arg_list, arg_count = self.parse_cmd(cmd_arg)

        if arg_count == 0:
            print("** class name missing **")
        elif arg_list[0] not in FileStorage.model_classes.keys():
            print("** class doesn't exist **")
        elif arg_count == 1:
            print("** instance id missing **")
        else:
            try:
                objs_dict = models.storage.all()
                storage_key = f"{arg_list[0]}.{arg_list[1]}"
                model_instance = objs_dict[storage_key]
                print(model_instance)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, cmd_arg):
        """
        Deletes an instance based on the class name and id (saves the change
        into the JSON file)

        example: $ destroy BaseModel 1234-1234-1234
        """
        arg_list, arg_count = self.parse_cmd(cmd_arg)

        if arg_count == 0:
            print("** class name missing **")
        elif arg_list[0] not in FileStorage.model_classes.keys():
            print("** class doesn't exist **")
        elif arg_count == 1:
            print("** instance id missing **")
        else:
            try:
                objs_dict = models.storage.all()
                storage_key = f"{arg_list[0]}.{arg_list[1]}"
                del objs_dict[storage_key]
                models.storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, cmd_arg):
        """
        prints all string representation of all instances based on or not on
        the class name
        """
        arg_list, arg_count = self.parse_cmd(cmd_arg)

        output_list = []
        objs_dict = models.storage.all()

        if arg_count == 0:
            for key, value in objs_dict.items():
                output_list.append(str(value))
        else:
            if arg_list[0] not in FileStorage.model_classes.keys():
                print("** class doesn't exist **")
            else:
                for key, value in objs_dict.items():
                    cls_name, id_ = key.split('.')
                    if cls_name == arg_list[0]:
                        output_list.append(str(value))

        if len(output_list) > 0:
            print(output_list)

    def do_count(self, cmd_arg):
        """
        retrieve the number of instances of a class
        """
        arg_list, arg_count = self.parse_cmd(cmd_arg)
        objs_dict = models.storage.all()
        count = 0

        if arg_list[0] not in FileStorage.model_classes.keys():
            print("** class doesn't exist **")
        else:
            for key, value in objs_dict.items():
                cls_name, id_ = key.split('.')
                if cls_name == arg_list[0]:
                    count += 1
        
        print(count)


    def do_update(self, cmd_arg):
        """
        updates an instance based on the class name and id by adding or
        updating attribute and saves the change into storage
        """
        arg_list, arg_count = self.parse_cmd(cmd_arg)
        if arg_count == 0:
            print("** class name missing **")
        elif arg_list[0] not in FileStorage.model_classes.keys():
            print("** class doesn't exist **")
        elif arg_count == 1:
            print("** instance id missing **")
        elif arg_count == 2:
            print("** attribute name missing **")
        elif arg_count == 3:
            print("** value missing **")
        else:
            objs_dict = models.storage.all()
            storage_key = f"{arg_list[0]}.{arg_list[1]}"
            try:
                model_inst = objs_dict[storage_key]
                attr_name = arg_list[2]
                attr_value = arg_list[3].strip("\"'")
                cur_attr_val = getattr(model_inst, attr_name, None)
                if cur_attr_val:
                    # cast update value to attribute type
                    attr_type = type(cur_attr_val)
                    attr_value = attr_type(attr_value)
                setattr(model_inst, attr_name, attr_value)
                model_inst.save()
            except KeyError:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
