#!/usr/bin/python3
"""Console to manage the server side
to storage engine
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    existing_class = {
                        "BaseModel": BaseModel, "User": User,
                        "Amenity": Amenity, "City": City, "Place": Place,
                        "Review": Review, "State": State
                    }

    # Do not show a prompt after each command read
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF   command to exit the program
        """
        return True

    def emptyline(self):
        """Funtion that clear the line command"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.existing_class:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.existing_class[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of
        an instance based on the class name and id"""
        new_dict = storage.all()
        tokenize = line.split(" ")
        count = 0
        if len(line) == 0:
            print("** class name missing **")
        elif tokenize[0] not in HBNBCommand.existing_class:
            print("** class doesn't exist **")
        elif len(tokenize) == 1:
            print("** instance id missing **")
        else:
            for key, value in new_dict.items():
                ids = key.split(".")
                if ids[1] == tokenize[1]:
                    print(value)
                    count = 1
            if count == 0:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        new_dict = storage.all()
        tokenize = line.split(" ")
        count = 0
        if len(line) == 0:
            print("** class name missing **")
        elif tokenize[0] not in HBNBCommand.existing_class:
            print("** class doesn't exist **")
        elif len(tokenize) == 1:
            print("** instance id missing **")
        else:
            link = tokenize[0] + "." + tokenize[1]
            if link in new_dict.keys():
                new_dict.pop(link)
                storage.save()
                count = 1
            if count == 0:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name"""
        new_dict = storage.all()
        list = []
        if len(line) == 0:
            for key, value in new_dict.items():
                list.append(str(value))
            print(list)
        elif line not in HBNBCommand.existing_class:
            print("** class doesn't exist **")
        else:
            for key, value in new_dict.items():
                clasess = key.split(".")
                if clasess[0] == line:
                    list.append(str(value))
            print(list)

    def do_update(self, line):
        """Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file)"""
        tokenize = line.split(" ")
        new_dict = storage.all()
        if len(tokenize) == 0:
            print("** class name missing **")
        elif tokenize[0] not in HBNBCommand.existing_class:
            print("** class doesn't exist **")
        elif len(tokenize) == 1:
            print("** instance id missing **")
        elif tokenize[0] + "." + tokenize[1] not in new_dict.keys():
            print("** no instance found **")
        elif len(tokenize) == 2:
            print("** attribute name missing **")
        elif len(tokenize) == 3:
            print("** value missing **")
        else:
            for key, value in new_dict.items():
                if (tokenize[0] + "." + tokenize[1]) == key:
                    setattr(value, tokenize[2], tokenize[3])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
