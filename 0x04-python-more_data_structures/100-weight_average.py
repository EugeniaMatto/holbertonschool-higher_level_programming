#!/usr/bin/python3
def weight_average(my_list=[]):
    res = 0
    total = 0
    for i, j in my_list:
        res += i * j
        total += j
    return res / total
