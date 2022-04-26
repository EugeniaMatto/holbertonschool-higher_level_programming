#!/usr/bin/python3
def uppercase(str):
    aux = 0
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            aux = i - 32
            print(f"{aux:c}", end="")
        else:
            print(f"{i:c}", end="")
