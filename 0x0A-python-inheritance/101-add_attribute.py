#!/usr/bin/python3
""" ex 13 """


def add_attribute(obj, attribute, value):
    """ add attribute """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
