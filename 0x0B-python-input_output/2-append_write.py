#!/usr/bin/python3
"""
Append a string at the end of a text file (UTF-8)
Return the no. of characters added
"""


def append_write(filename="", text=""):
    """use open(), write()"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
