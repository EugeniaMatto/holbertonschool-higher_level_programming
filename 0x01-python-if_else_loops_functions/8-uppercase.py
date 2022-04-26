#!/usr/bin/python3
def uppercase(str):
    aux = 0
    for i in str:
        aux = ord(i)
        if aux > 96 and aux < 123:
            aux -= 32
        print(f"{aux:c}", end="")
    print()
