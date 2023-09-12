#!/usr/bin/python3
"""
Module 10-student

Contains class Student
that initializes public instance attributes first_name, last_name, and age,
and has public method to_json that retrieves its dictionary representation
"""


class Student:
    """
    Public Attributes:
        first_name
        last_name
        age

    Public methods:
        to_json : returns dict description of the object
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes Student instance with fullname and age

        Args:
            first_name,
            last_name,
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary description with simple data structure
        (list, dictionary, dictionary, string)
        for JSON serialization of an object. If `attrs` is a list of strings,
        only attributes names contained in the list must be retrieved.

        Args:
            attrs : list of attribute names to retrieve or None
        """
        if attrs:
            attr_dic = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    attr_dic[attr] = self.__dict__[attr]
            return attr_dic
        return self.__dict__
