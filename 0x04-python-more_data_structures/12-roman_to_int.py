#!/usr/bin/python3
def roman_to_int(roman_string):
    suma = 0
    if (isinstance(roman_string, str) and roman_string):
        for i in roman_string:
            if ((i != 'I') and (i != 'V') and (i != 'X') and
            (i != 'L') and (i != 'C') and (i != 'D') and (i != 'M')):
                return 0
        roman_string += "-"
        for i in range(len(roman_string) - 1):
            if roman_string[i] == 'I':
                if roman_string[i + 1] == 'V' or roman_string[i + 1] == 'X':
                    suma -= 1
                else:
                    suma += 1
            if roman_string[i] == 'V':
                suma += 5
            if roman_string[i] == 'X':
                if roman_string[i + 1] == 'L' or roman_string[i + 1] == 'C':
                    suma -= 10
                else:
                    suma += 10
            if roman_string[i] == 'L':
                    suma += 50
            if roman_string[i] == 'C':
                suma += 100
            if roman_string[i] == 'D':
                if roman_string[i + 1] == 'M':
                    suma -= 500
                else:
                    suma += 500
            if roman_string[i] == 'M':
                suma += 1000
        roman_string = roman_string[:-1]
    return suma
