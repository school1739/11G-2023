n = int(input("Введите размер квадратной матрицы: "))
matrix = [[0] * n for i in range(n)]
print(matrix)
shape = int(input("Введите размер матрицы (должно быть числом в квадрате): "))
if shape == 1:
    matrix = [[1]]
    print(matrix)
elif shape == 2:
    matrix = [[1, 2], [3, 4]]
    print(matrix)
elif shape == 3:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix)
elif shape == 4:
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(matrix)
else:
    matrix = [[0] * shape for i in range(shape)]
    for row in matrix:
        print(row)


def minor(a):
    return [[a[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def calculate_det(matrix):
    det = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            det += matrix[i][j] * minor(matrix)[i][j]
    return det


print(calculate_det(matrix))
