#!/usr/bin/python3
"""
class: Student
Public instance attributes: first_name, last_name, age
Constrictor--> first_name, last_name & age
Public method--> to_json(self): --> dict representation of a Student instance
Donts: import any module
"""


class Student:
    """Constructor"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """public method to_json(self):"""
    def to_json(self):
        """retrieves a dict represenation of a Student instance"""
        return self.__dict__
