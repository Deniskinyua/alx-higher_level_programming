#!/usr/bin/python3
"""
returns true if object is exactly an instance of the specified class else false
"""


def is_same_class(obj, a_class):
    """object exactly an instance of specified class ? true : false"""
    return (type(obj) == a_class)
