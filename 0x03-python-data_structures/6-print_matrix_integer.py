#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            print(f"{j:d}", end="")
            if (j != i[-1]):
                print(" ", end="")
        print()
