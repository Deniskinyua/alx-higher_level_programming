#!/usr/bin/python3
"""
Function that reads a text file (UTF8)
Print it to stdou
"""


def read_file(filename=""):
    """function: use open() and read()"""
    f = open(filename, mode='r', encoding='utf-8')
    print(f.read(), end="")
