#!/usr/bin/python3
"""
LockedClass --> no class/object attribute
"""


class LockedClass:
    """ No class or object attributes
    """
    def __setattr__(self, attribute, value):
        if attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + attribute + "'")
