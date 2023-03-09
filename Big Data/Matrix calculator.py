# Ягупов Горбатенков
def get_matrix():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix.append(row)
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = int(input("Введите элемент [{},{}]: ".format(i, j)))
    return matrix

def minor(matrix, i, j):
    minor = []
    for k in range(len(matrix)):
        if k != i:
            row = []
            for l in range(len(matrix[0])):
                if l != j:
                    row.append(matrix[k][l])
            minor.append(row)
    return minor

def determinant(matrix):
    n = len(matrix)
    det = 0
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for i in range(n):
            det += ((-1) ** (i+j)) * matrix[0][i] * determinant(minor(matrix, 0, i))
        return det

print("Калькулятор определителя матриц и её минора")
matrix = get_matrix()

i = int(input("Введите строку минора: "))
j = int(input("Введите столбец минора: "))
minor_matrix = minor(matrix, i, j)
print("Минор:")
for row in minor_matrix:
    print(row)
det = determinant(matrix)
print(f"Определитель матрицы: {det}")



















'''def get_matrix():
    # Получение матрицы от пользователя
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix.append(row)
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = float(input("Введите элемент [{},{}]: ".format(i, j)))
    return matrix

def determinant(matrix):
    # Функция для вычисления определителя матрицы
    n = len(matrix)
    det = 0
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for i in range(n):
            minor = []
            for j in range(1, n):
                row = []
                for k in range(n):
                    if k != i:
                        row.append(matrix[j][k])
                minor.append(row)
            det += ((-1) ** i) * matrix[0][i] * determinant(minor)
        return det

print("Калькулятор определителя матриц")
matrix = get_matrix()
det = determinant(matrix)
print(f"Определитель матрицы: {det}'''





















