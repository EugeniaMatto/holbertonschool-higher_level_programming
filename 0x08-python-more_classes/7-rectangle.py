#!/usr/bin/python3
"""··· >>>Class Rectangle<<< ···"""


class Rectangle:
    """ ···Define Rectangle··· """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ init class """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ returns the rectangle area """
        return (self.__height * self.__width)

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ print rectangle, override str """
        h = self.__height
        w = self.__width
        if h != 0 and w != 0:
            for i in range(h):
                for j in range(w):
                    print(self.print_symbol, end="")
                if (i < h - 1):
                    print()
        return ""

    def __repr__(self):
        """ override repr """
        return (f"Rectangle({self.__width:d}, {self.__height:d})")

    def __del__(self):
        """ override del """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
