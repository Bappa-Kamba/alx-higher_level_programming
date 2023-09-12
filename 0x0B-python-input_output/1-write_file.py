#!/usr/bin/python3
"""
Module 1-write_file

Contains function to write to a file. It creates it if not present.
"""


def write_file(filename="", text=""):
    """
    Returns number of characters written to the file

    Args:
        filename : File,
        text : String to write
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
