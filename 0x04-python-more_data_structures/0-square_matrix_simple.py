#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return (list(list(map(lambda x: x*x, num)) for num in matrix))
