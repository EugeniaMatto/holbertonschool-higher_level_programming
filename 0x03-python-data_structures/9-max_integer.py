#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max = -9999999
    for i in my_list:
        if i > max:
            max = i
    return max
