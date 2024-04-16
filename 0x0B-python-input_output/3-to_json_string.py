#!/usr/bin/python3
"""
Function that returns JSON representation of an object(string)
Dont need to manage expectations if the object cant be serialized
"""

import json

def to_json_string(my_obj):
    """ use json.dumps()"""
    return json.dumps(my_obj)
