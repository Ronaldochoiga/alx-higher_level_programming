#!/usr/bin/python3
"""Module matrix_mul - Multiplies two matrices and returns the result.
"""


def matrix_mul(m_a, m_b):
    """Return the matrix resulting of
    the multiplication of m_a and m_b."""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for a in m_a:
        if type(a) is not list:
            raise TypeError("m_a must be a list of lists")
    for a in m_b:
        if type(a) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for a in row:
            if type(a) is not int and type(a) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for a in row:
            if type(a) is not int and type(a) is not float:
                raise TypeError("m_b should contain only integers or floats")

    row_len = []
    for row in m_a:
        row_len.append(len(row))
    if not all(elem == row_len[0] for elem in row_len):
            raise TypeError("each row of m_a must should be of the same size")
    row_len = []
    for row in m_b:
        row_len.append(len(row))
    if not all(elem == row_len[0] for elem in row_len):
            raise TypeError("each row of m_b must should be of the same size")

    a_col = 0
    for col in m_a[0]:
        a_col += 1
    b_row = 0
    for row in m_b:
        b_row += 1

    if a_col != b_row:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for a in range(len(m_b[0]))] for y in range(len(m_a))]

    for b in range(len(m_a)):
        for c in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[b][c] += m_a[b][k] * m_b[k][c]

    return result
