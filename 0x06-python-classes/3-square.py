#!/usr/bin/python3
"""Class Square"""


class Square:
    """define Square"""

    def __init__(self, size=0):
        """Init square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area Square"""
        return (self.__size * self.__size)
