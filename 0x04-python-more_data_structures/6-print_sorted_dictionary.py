#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted(list(a_dictionary)):
        print(f"{i}: {a_dictionary[i]}")
