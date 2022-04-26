#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    aux = number % 10
    print(f"{aux:d}", end="")
    return aux
