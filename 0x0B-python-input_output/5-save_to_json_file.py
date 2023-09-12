#!/usr/bin/python3
"""
Module 5-save_to_json_file

Contains funtion that writes an Object to a file using JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    function to write an Object to a file using JSON representation

    Args:
        my_obj : Python object,
        filename : File to write to
    """
    with open(filename, mode='w', encoding='utf-8')as myFile:
        json.dump(my_obj, myFile)
