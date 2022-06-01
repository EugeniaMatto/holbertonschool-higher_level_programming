#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """Write a function that inserts a line of text to a file"""
    with open(filename, 'r') as j:
        a = j.readlines()

        with open(filename, 'w') as b:

            for line in a:
                b.write(line)
                if search_string in line:
                    b.write(new_string)
