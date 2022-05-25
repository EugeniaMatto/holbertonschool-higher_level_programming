#!/usr/bin/python3
""" module ex 100 advanced
"""


def matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    ma_f, mb_f, ma_el, mb_el = 0, 0, 0, 0
    ma_s, mb_s = 0, 0
    for i in m_a:
        if type(i) != list:
            raise TypeError("m_a must be a list of lists")
        if i != []:
            ma_f = 1
        for j in i:
            if type(j) != int and type(j) != float:
                ma_el = 1
        if len(i) != len(m_a[0]):
            ma_s = 1
    for i in m_b:
        if type(i) != list:
            raise TypeError("m_b must be a list of lists")
        if i != []:
            mb_f = 1
        for j in i:
            if type(j) != int and type(j) != float:
                mb_el = 1
        if len(i) != len(m_b[0]):
            mb_s = 1
    if m_a == [] or ma_f == 0:
        raise ValueError("m_a can't be empty")
    if m_b == [] or mb_f == 0:
        raise ValueError("m_b can't be empty")
    if ma_el == 1:
        raise TypeError("m_a should contain only integers or floats")
    if mb_el == 1:
        raise TypeError("m_b should contain only integers or floats")
    if ma_s == 1:
        raise TypeError("each row of m_a must be of the same size")
    if mb_s == 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new = []
    new_fi = len(m_a)
    new_col = len(m_b[0])
    for i in range(new_fi):
        new.append([])
    for i in range(len(new)):
        for j in range(new_col):
            res = 0
            for k in range(len(m_b)):
                res += m_a[i][k] * m_b[k][j]
            new[i].append(res)
    return new
