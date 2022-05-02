#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print(f"{matrix[i][j]}", end="")
            if (j != len(matrix) - 1):
                print(" ", end="")
        if (i != len(matrix[0]) - 1):
            print()
    print()
