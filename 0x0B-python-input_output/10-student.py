#!/usr/bin/python3
"""
class Student
public instances: first_name, last_name, age
constructor: public instances
public method: def to_json(self, attr=None)
condition: if attrs == list of strings, retrive attribute names
           else: retrieve all
Donts: imports1
"""


class Student:
    """constructor"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """only attribute names if attrs is a list of strings, else all"""
        if attrs is None:
            return self.__dict__
        dictr = {}
        for i in attrs:
            try:
                dictr[i] = self.__dict__[i]
            except (KeyError, TypeError):
                pass
        return dictr
