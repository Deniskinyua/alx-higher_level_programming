#!/usr/bin/python3
"""
adds 2 integers --> a + b
"""


def add_integer(a, b=98):
    """adding a and b -->"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer or float")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer or float")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
