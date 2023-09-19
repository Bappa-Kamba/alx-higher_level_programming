#!/usr/bin/python3

'''
Module contain class Base

Base class in the package
'''

import json


class Base():
    """
    Base class of all subsequent classes.

    Class attributes:
        __nb_objects

    Methods:
        __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor to initialize `id` if not None; otherwise, increment
        `__nb_objects` and assign to `id`
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of `list_dictionaries`:
            `list_dictionaries` is a list of dictionaries;
            If `list_dictionaries` is `None` or empty, return the
            string: `"[]"`;
            Otherwise, return the JSON string representation of
            `list_dictionaries`.
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of `list_objs` to a file:
            * `list_objs` is a list of instances who inherits `Base`
                - example: list of `Rectangle` or list of `Square` instances
            * If `list_objs` is `None`, save an empty list
            * The filename must be: `<Class name>.json` - example:
            `Rectangle.json`
            * You must use the static method `to_json_string` (created before)
            * You must overwrite the file if it already exists

        Note: before converting `list_objs` to string, first use the
        `to_dictionary`
            method of the instances to create a dictionary first
        """

        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
            filename = cls.__name__ + ".json"
            target = cls.to_json_string(objs)
            with open(filename, mode="w", encoding="utf-8")as file:
                file.write(target)
        else:
            filename = cls.__name__ + ".json"
            with open(filename, mode="w", encoding="utf-8")as file:
                file.write("[]")

    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string:
            * json_string is a string representing a list of dictionaries
            * If json_string is None or empty, return an empty list
            * Otherwise, return the list represented by json_string
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set:
            * `**dictionary` can be thought of as a double pointer to a
                dictionary
            * To use the `update` method to assign all attributes, you must
                create a `“dummy”` instance before:
            * Create a `Rectangle` or `Square` instance with `“dummy”`
                mandatory
                attributes (`width`, `height`, `size`, etc.)
            * Call `update` instance method to this `“dummy”` instance to apply
                your real values
            * You must use the method def `update(self, *args, **kwargs)`
            * `**dictionary` must be used as `**kwargs` of the method `update`
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances:
            * The filename must be: `<Class name>.json` - example:
            `Rectangle.json`
            * If the file doesn't exist, return an empty list
            * Otherwise, return a list of instances - the type of these
            instances
                depends on `cls` (current class using this method)
            * You must use the `from_json_string` and `create` methods
            (implemented previously)
        """
        filename = cls.__name__ + ".json"

        list = []
        try:
            with open(filename, 'r') as file:
                read_file = file.read()
                instance_list = cls.from_json_string(read_file)
                for instance in instance_list:
                    list.append(cls.create(**instance))
        except FileNotFoundError:
            list = []
            return list

        return list
