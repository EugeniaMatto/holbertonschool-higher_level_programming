#!/usr/bin/python3
def best_score(a_dictionary):
    max = -255
    nombre = None
    if a_dictionary:
        for i in list(a_dictionary):
            if (a_dictionary[i] > max):
                max = a_dictionary[i]
                nombre = i
    return nombre
