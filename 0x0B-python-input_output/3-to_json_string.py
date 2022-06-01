#!/usr/bin/python3
"""JSON"""


import json


def to_json_string(my_obj):
    """str to json"""
    oJSON = json.dumps(my_obj)
    return oJSON
