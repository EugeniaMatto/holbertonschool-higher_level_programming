#!/usr/bin/python3
""" Ex. 1 """


class MyList(list):
    """ class MyList """
    pass

    def print_sorted(self):
        """ print sorted function """
        new = self.copy();
        for i in range(len(new) - 1):
            if new[i] > new[i + 1]:
                aux = new[i]
                new[i] = new[i + 1]
                new[i + 1] = aux
        print(new)
