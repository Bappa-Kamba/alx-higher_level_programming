#!/usr/bin/python3
"""
Module 3-to_json_string

Contains function that returns a JSON representation of a Python object
"""

import json


def to_json_string(my_obj):
    """
    Returns a JSON representation of the object

    Args:
        my_obj : Python object
    """
    return json.dumps(my_obj)
