#!/usr/bin/python3
"""
Only subclass of
"""


def inherits_from(obj, a_class):
    """obj of instance of a class inherited from the specified class? --> true`"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
