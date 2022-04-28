#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    le = len(sys.argv) - 1
    suma = 0
    for i in sys.argv:
        if i != "./3-infinite_add.py":
            suma += int(i)
    print(f"{suma}")

