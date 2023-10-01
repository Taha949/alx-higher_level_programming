#!/usr/bin/python3
"""Containing append_after"""


def append_after(filename="", search_string="", new_string=""):
    """function 

    Args:
        filename (str, optional): file’s name"".
        search_string (str, optional): what string we are searching for .
        new_string (str, optional): string to append """
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fo.write(s)
