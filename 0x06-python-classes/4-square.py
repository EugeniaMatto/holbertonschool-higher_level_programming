#!/usr/bin/python3
"""Class Square"""


class Square:
    """Define Square"""

    def __init__(self, size=0):
        """ Init Square """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """ Size Square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Area Square """
        return (self.__size * self.__size)
