#!/usr/bin/python3
""" >>>Class Rectangle<<< """


class Rectangle:
    """ ···Define Rectangle··· """

    def __init__(self, width=0, height=0):
        """ init function """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get height """
        return sef.__self

    @height.setter
    def height(self, value):
        """ setter height """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
