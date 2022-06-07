#!/usr/bin/python3
""" ex 0 """


import json


class Base:
    """ class Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if (id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string """
        a = "[]"
        if (list_dictionaries is not None and
                list_dictionaries):
            a = "["
            for i in list_dictionaries:
                a += json.dumps(i)
                a+= ", "
            a += "]"
        return a
