#!/usr/bin/python3
""" Ex. 1 """


class MyList(list):
    """ class MyList """
    pass

    def print_sorted(self):
        """ print sorted function """
        new = self.copy()
        new.sort()
        print(new)
