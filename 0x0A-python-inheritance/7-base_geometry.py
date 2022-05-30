#!/usr/bin/python3
""" empty class BaseGeometry """


class BaseGeometry:
    """ BaseGeometry """
    pass

    def area(self):
        """ area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
