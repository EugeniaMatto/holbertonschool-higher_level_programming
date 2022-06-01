#!/usr/bin/python3
"""Load, add, save"""


import json
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

data = list()

if os.path.exists("add_item.json"):
    data = load_from_json_file("add_item.json")

for i in sys.argv:
    if i is sys.argv[0]:
        continue
    data.append(i)
save_to_json_file(data, "add_item.json")
