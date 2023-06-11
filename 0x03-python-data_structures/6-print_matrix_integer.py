#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix and len(matrix[0]):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print("{}".format(matrix[i][j]), end=' ' if j < len(matrix) - 1 else '')
            print()
