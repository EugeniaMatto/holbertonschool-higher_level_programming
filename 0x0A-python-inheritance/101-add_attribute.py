#!/usr/bin/python3
""" ex 13 """

def add_attribute(obj, attribute, value):
    if ("__dict__" is not dir(obj)):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
