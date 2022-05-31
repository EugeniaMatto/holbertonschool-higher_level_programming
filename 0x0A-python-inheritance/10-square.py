#!/usr/bin/python3
""" Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square """

    def __init__(self, size):
        """ init square """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ area """
        super().area()

    def __str__(self):
        """ str """
        super().__str__()
