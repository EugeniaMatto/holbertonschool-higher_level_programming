#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (my_list is None or idx < 0 or idx > (len(my_list) - 1)):
        return my_list
    b = my_list.copy()
    b[idx] = element
    return b
