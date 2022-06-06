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
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if (type(value) != int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if (type(value) != int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area """
        return self.__height * self.__width

    def display(self):
        """ prints in stdout the rectangle instance with #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def __str__(self):
        """ override str """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} " +
                f"- {self.__width}/{self.__height}")

    def update(self, *args):
        """ update function """
        l = len(args)
        if (l > 0):
            self.id = args[0]
        if (l > 1):
            self.__width = args[1]
        if (l > 2):
            self.__height = args[2]
        if (l > 3):
            self.__x = args[3]
        if (l > 4):
            self.__y = args[4]
