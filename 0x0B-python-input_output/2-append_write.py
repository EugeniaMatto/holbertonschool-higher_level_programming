#!/usr/bin/python3
""" function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """append text to a txt"""
    with open(filename, 'a+') as txt:
        num = txt.write(text)
        return num
