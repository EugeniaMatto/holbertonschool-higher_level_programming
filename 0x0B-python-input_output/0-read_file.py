#!/usr/bin/python3
"""input output function"""


def read_file(filename=""):
    """read a file and print to stdout"""
    with open(filename, 'r', encoding="utf-8") as a:
        print(a.read(), end="")
