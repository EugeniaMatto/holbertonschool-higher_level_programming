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
        if (list_dictionaries is None or
                len(list_dictionaries) == 0):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs """
        filename = cls.__name__ + ".json"
        a = []
        for i in list_objs:
            a.append(i.to_dictionary())
        if a == []:
            a = "[]"
        else:
            a = cls.to_json_string(a)
        with open(filename, 'w') as txt:
            txt.write(a)
