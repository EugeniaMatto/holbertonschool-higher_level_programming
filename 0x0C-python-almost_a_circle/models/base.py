#!/usr/bin/python3
""" ex 0 """


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
