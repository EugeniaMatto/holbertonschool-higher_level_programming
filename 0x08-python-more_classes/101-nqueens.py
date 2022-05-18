#!/usr/bin/python3
""" ··· N queens ··· """
import sys

av = sys.argv
ac = len(av)

if (ac != 2):
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(av[1])
except Exception:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

""" solutions: n - 2 (all positions but borders) """
nums = []
for i in range(n + 1):
    nums.append(i)

""" second position always start in 3 y va sumando de a 2
    en horizontal la segunda posicion"""
start = 3
""" second position increments this way: {2, 3, 4, ..., N} in vertical
    in bucle hasta N(ex. N = 6,
    si incremento de a 2 y soy 5 entonces quedo 0)"""
i = 2
""" solution number """
solN = 0
sol = []
while(solN < n - 2):
    sol.append([])
    for j in range(n):
        sol[solN].append([j, '-'])
    sol[solN][0][1] = solN + 1
    solN += 1
""" sol[solN][pos][[i],[j]] """
pos = 1
while(pos < n):
    sc = start
    solN = 0
    for solN in range(0, n - 2):
        sol[solN][pos][1] = sc
        for x in range(i):
            sc += 1
            if sc > n:
                sc = 0
    for t in range(2):
        start += 1
        if (start > n):
            start = 0
    i += 1
    pos += 1

for i in sol:
    print(i)
