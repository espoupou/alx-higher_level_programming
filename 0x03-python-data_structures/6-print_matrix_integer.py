#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix and len(matrix[0]):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if j != 0:
                    print(" ", end='')
                print("{:d}".format(matrix[i][j]), end='')
            print()
