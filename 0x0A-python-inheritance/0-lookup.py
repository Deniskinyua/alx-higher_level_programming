#!/usr/bin/python3
"""
Returns a list of available attributes and methods of an object
"""


def lookup(obj):
    """return list of attributes and methods of an object"""
    return dir(obj)
