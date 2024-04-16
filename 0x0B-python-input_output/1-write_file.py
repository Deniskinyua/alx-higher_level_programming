#!/usr/bin/python3
"""
Write a string to a text file (UTF-8)
Return the number of characters written
"""


def write_file(filename="", text=""):
    """Use open(), write(), mode='w'"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
