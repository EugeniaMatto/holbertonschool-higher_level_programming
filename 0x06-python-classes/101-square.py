#!/usr/bin/python3
"""Class Square"""


class Square:
    """Define Square"""

    def __init__(self, size=0, position=(0, 0)):
        """ Init Square """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """ Size Square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter position"""
        if (type(value) != tuple or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Area Square """
        return (self.__size * self.__size)

    def my_print(self):
        """ Print Square """
        if (self.__size > 0):
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    def __str__(self):
        """override __str__"""
        if (self.__size > 0):
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                if (i != (self.__size - 1)):
                    print()
  
        return ""
