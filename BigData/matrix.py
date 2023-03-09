from random import *
shape = int(input())
matrix = [[2, 4, 1, 1], [0, 2, 0, 0], [2, 1, 1, 3], [4, 0, 2, 3]]
def Minor(matrix, i, j):
    A = matrix.copy()
    del A[i]
    for n in range(shape - 1):
        del A[n][j]
    return A

def Det(matrix):
    summ = 0
    for j in range(4):
        A = Minor(matrix, 0, j)
        summ += A[0][0]*A[1][1]*A[2][2]+A[0][1]*A[1][2]*A[2][0]


