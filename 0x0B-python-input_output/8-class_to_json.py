#!/usr/bin/python3
"""
Module 9-class_to_json

Contains function that returns dictionary description with simple data
structures (list, dictionary, string, integer and boolean) for
JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj : Python object
    """
    return obj.__dict__
