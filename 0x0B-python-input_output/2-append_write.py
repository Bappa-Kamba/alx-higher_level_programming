#!/usr/bin/python3
"""
Module 2-append_write

Contains funtion to append a string to a file.
"""


def append_write(filename="", text=""):
    """
    Returns the number of characters appended to the file

    Args:
        filename : file,
        text : string to append
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
