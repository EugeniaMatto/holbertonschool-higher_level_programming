#!/usr/bin/python3
""" Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square """

    def __init__(self, size):
        """ init square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return (f"[Square] <{self.__size}>/<{self.__size}>")
