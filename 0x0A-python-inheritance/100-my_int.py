#!usr/bin/python3
""" ex 12 """


class MyInt(int):
    """ My int """

    def __eq__(self, other):
        """ override eq """
        return super().__ne__(other)

    def __ne__(self, other):
        """ override ne """
        return super().__eq__(other)
