#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if my_list == [] or x == 0:
            print()
            return 0
        for i in range(x):
            print(my_list[i], end="" if i != x - 1 else "\n")
        return x
    except IndexError:
        print()
        return i
