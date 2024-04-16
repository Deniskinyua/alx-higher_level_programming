#!/usr/bin/python3
"""
Function: returns an object (Python DS) represented by a JSON string
Dont need to manage expectations if the JSON string doesnt represent an obj
"""


import json


def from_json_string(my_str):
    """use json.loads()"""
    return json.loads(my_str)
