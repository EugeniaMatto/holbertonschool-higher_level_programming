#!/usr/bin/python3
def remove_char_at(str, n):
    if n > -1 and n < len(str):
        str = f"{str[:n]}{str[n+1:]}"
    return str
