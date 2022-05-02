#!/usr/bin/python3
def max_integer(my_list=[]):
    new = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new[i] = True
        else:
            new[i] = False
    return new
