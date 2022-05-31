#!usr/bin/python3
""" ex 12 """


class MyInt(int):
    """ My int """

    def __init__(self, n):
        """ init """
        super().__init__()
        self.__n = n

    def __eq__(self, other):
        """ override eq """
        return self.__n != other

    def __ne__(self, other):
        """ override ne """
        return self.__n == other
