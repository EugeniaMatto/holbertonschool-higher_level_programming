#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """new class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            newd = {}
            for i in attrs:
                for key, value in self.__dict__.items():
                    if key == i:
                        newd[key] = value
            return newd
        return self.__dict__

    def reload_from_json(self, json):
        self.__dict__.update(json)
