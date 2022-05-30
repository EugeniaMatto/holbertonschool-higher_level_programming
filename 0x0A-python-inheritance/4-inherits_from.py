#!/usr/bin/python3
""" ex 4 """


def inherits_from(obj, a_class):
    """ inherits_from """
    return isinstance(obj, a_class) and (type(obj) != a_class)
