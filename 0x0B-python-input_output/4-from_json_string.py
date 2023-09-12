#!/usr/bin/python3
"""
Module 4-from_json_string

Contains function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns Python data structure from JSON string

    Args:
        my_str : JSON string to load
    """
    return json.loads(my_str)
