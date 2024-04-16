#!/usr/bin/python3
"""
Function: create an Object from a "JSON file"
Must: use 'with'
Donts: Need to manage expectations if the JSON String doesnt rep an obj
Donts: Need to manage file permissions/exceptions
"""


import json


def load_from_json_file(filename):
    """Use open() & json.load()"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
