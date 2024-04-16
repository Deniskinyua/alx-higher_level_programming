#!/usr/bin/python3
"""
Script: Add all arguments to a Python list, save them to a file:
Must: use the function load_from_json_file from 6_load_from_json_file.py
Must: use your function save_to_json_file from 5-save_to_json_file.py
Must: save the list as a JSON representation in a file names add_item.json
Condition: If file does not exist its should be created
Donts: Need to manage file permissions/exceptions
"""


import sys
"""load"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""save it"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    loadedfile = load_from_json_file("add_item.json")
except FileNotFoundError:
    loadedfile = []

ln = len(sys.argv)
for x in range(1, ln):
    loadedfile.append(sys.argv[x])
save_to_json_file(loadedfile, "add_item.json")
