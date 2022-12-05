#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    mat_len = len(matrix)
    for i in range(mat_len):
        for j in range(len(matrix[i])):
            if (j != i[-1]):
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]), end="")
        print("")
