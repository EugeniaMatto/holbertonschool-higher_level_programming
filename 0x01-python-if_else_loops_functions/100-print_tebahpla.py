#!/usr/bin/python3
for i in reversed(range(97, 123)):
    ch = i
    if i % 2 == 1:
        ch = ch - 32
    print(f"{ch:c}", end="")
