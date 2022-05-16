#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    else:
        print("Inside result: ", result)
    finally:
        return result
