#!/usr/bin/python3
def roman_to_int(roman_string):
    suma = 0
    if (isinstance(roman_string, str) and roman_string):
        for i in roman_string:
            if i == 'I':
                suma += 1
            if i == 'V':
                suma += 5
            if i == 'X':
                suma += 10
            if i == 'L':
                suma += 50
            if i == 'C':
                suma += 100
            if i == 'D':
                suma += 500
            if i == 'M':
                suma += 1000
    return suma
