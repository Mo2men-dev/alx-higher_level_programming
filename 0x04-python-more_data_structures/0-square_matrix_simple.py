#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_mtrx = []
    for i in matrix:
        new_mtrx.append(list(map(lambda x: x**2, i)))
    return new_mtrx
