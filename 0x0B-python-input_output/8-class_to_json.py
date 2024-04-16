#!/usr/bin/python3
"""
Function: Return the dictionary description with simple data structure
DS could be: list, dictionary, string,
or integer and boolean for JSON serialization of an onj
'obj' is an instance of a class
All attribytes of obj class are serializable:-->
 list, dictionar, string, integer and boolean
Donts: import any module
"""


def class_to_json(obj):
    """use __dict__"""
    return obj.__dict__
