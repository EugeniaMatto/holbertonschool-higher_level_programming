#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    b = my_list.copy()
    b.reverse()
    for i in b:
        print(f"{i:d}")
