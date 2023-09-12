#!/usr/bin/python3
"""
Module 6-load _from_json

Contains function to create an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Returns a python object from a file.

    Args:
        filename : file
    """
    with open(filename, encoding='utf-8') as myFile:
        return json.load(myFile)
