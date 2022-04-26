#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    return(number % 10)
