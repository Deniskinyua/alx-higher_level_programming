#!/usr/bin/python3
"""
Function: writes an Object to a text file using a JSON representation
Must: use the 'with' statement
Dont: Need to manage expecations if obj cant be serialized
Dont: Need to manage file permission exceptions
"""


import json


def save_to_json_file(my_obj, filename):
    """use open(), json.dump()"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
