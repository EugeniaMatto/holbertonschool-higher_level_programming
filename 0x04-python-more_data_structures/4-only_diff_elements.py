#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    s1 = set_1.difference_update(set_2)
    s2 = set_2.difference_update(set_1)
    return s1.update(s2)
