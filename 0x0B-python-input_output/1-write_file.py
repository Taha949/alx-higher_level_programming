#!/usr/bin/python3
"""Contains write_file"""


def write_file(filename="", text=""):
    """Input strings outpu characters

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): string of text to write to file. Defaults to "".

    Returns:
        int: characters'length
    """
    with open(filename, 'w', encoding="utf-8") as f:
        """Returning characters"""
        return f.write(text)
