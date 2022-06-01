#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascals triangle of n 
    """
    lis = [[1]]
    if n <= 0:
        lis.clear()
        return lis
    if n == 1:
        return lis
    i = 0
    while (len(lis[i]) != n):
        lis.append([])
        i += 1
        for j in range(len(lis[i - 1]) + 1):
            lis[i].append(1)
        if len(lis[i]) > 2:
            for k in range(1, len(lis[i]) - 1):
                lis[i][k] = lis[i - 1][k - 1] + lis[i - 1][k]
    return lis
