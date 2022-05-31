#!/usr/bin/python3
""" empty class BaseGeometry """


class BaseGeometry:
    """ BaseGeometry """

    def __init__(self, width, height):
        """ init """
        self.integer_validator(self, width)
        self.integer_validator(self, height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
