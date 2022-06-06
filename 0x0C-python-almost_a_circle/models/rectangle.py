#!/usr/bin/python3
""" ex 2 """


from models.base import Base


class Rectangle(Base):
    """ class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width """
        self.__width = value

    @property
    def height(self):
        """ getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
