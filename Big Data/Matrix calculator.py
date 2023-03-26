# Ягупов Горбатенков
shape = int(input('Введите размер матрицы: '))
matrix = []
for i in range(shape):
    matrix.append([])
    for j in range(shape):
        matrix[i].append(int(input(f'Введите число, место ({i+1}, {j+1}): ')))


def minor(matrix, i, j):
    minor_matrix = [buff.copy() for buff in matrix]
    del minor_matrix[i-1]

    for i in range(len(minor_matrix)):
        del minor_matrix[i][j-1]
    return minor_matrix


def calculate_det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        print(matrix)
        det = 0
        for j in range(len(matrix)):
            det += ((-1)**j)*matrix[0][j]*calculate_det(minor(matrix, 1, j+1))
    return det


print(calculate_det(matrix))




















