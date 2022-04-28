#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    le = len(sys.argv) - 1
    print(f"{le:d} ", end="")
    if (le == 0):
        print("arguments.")
    if (le > 1):
        print("arguments:")
    if (le == 1):
        print("argument:")
    x = 0
    for i in sys.argv:
        if i != "./2-args.py":
            x += 1
            print(f"{x}: {i}")
