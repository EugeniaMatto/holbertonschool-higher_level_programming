#!/usr/bin/python3
""" ··· N queens ··· """
import sys


def _init():
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

    NQueens(n)


def is_valid(chess, n, lvl):
    for i in range(lvl):
        if chess[i] == chess[lvl]:
            return False
        if abs(lvl - i) == abs(chess[i] - chess[lvl]):
            return False
    return True


def NQueens_R(chess, n, lvl):
    if n == lvl:
        outp = []
        for i in range(n):
            outp.append([i, chess[i]])
        print(outp)
    else:
        chess[lvl] = 0
        while(chess[lvl] < n):
            if is_valid(chess, n, lvl):
                NQueens_R(chess, n, lvl + 1)
            chess[lvl] += 1


def NQueens(n):
    lvl = 0
    chess = []
    for i in range(n):
        chess.append(-1)

    NQueens_R(chess, n, lvl)


if __name__ == "__main__":
    _init()
