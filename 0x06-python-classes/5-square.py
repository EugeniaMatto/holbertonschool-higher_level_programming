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

    def my_print(self):
        """ Print Square """
        if (self.__size > 0):
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
