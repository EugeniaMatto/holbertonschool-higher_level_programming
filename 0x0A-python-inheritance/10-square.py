#!/usr/bin/python3
""" Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

Rectangle = __import__('9-rectangle').Rectangle

class Square:
    """ square """

    def __init__(self, size):
        super().__init__()
        self.__size = size
