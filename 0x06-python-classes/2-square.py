#!/usr/bin/python3
"""Class Square"""

class Square:
    """Define Square"""

    def __init__(self, size=0):
        """Init Class"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
