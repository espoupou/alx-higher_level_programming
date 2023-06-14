#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = matrix.copy()
    for i in range(len(mat)):
        mat[i] = list(map(lambda x: x**2, mat[i]))
    return mat
