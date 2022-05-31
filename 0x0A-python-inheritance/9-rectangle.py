#!/usr/bin/python3
""" Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle """

    def __init__(self, width, height):
        """ init """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area """
        return self.__width * self.__height

    def __str__(self):
        """ str """
        return (f"[Rectangle] {self.__width}/{self.__height}")
