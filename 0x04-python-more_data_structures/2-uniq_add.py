#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    new = []
    for i in my_list:
        try:
            new(i)
        except ValueError:
            add += i
        new.append(i)
    return add
