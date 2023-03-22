#Авторы : Гончаров
import copy

'''
Matrix = [[ 1,  2,  3,  4],
          [-1, -2, -3, -4],
          [ 0,  1,  1,  0],
          [ 1,  0,  0,  1]]
'''

def InputMatrix(size):
    matrix = []
    for i in range(size):
        matrix.append([i for i in range(size)])
        for j in range(size):
            matrix[i][j] = int(input(f"a{i+1}{j+1} : "))
    return matrix

''' Тест InputMatrix()
print(InputMatrix(int(input("Введите размер матрицы : "))))
'''

def MinorMatrix(matrix, i, j):
    newMatrix = copy.deepcopy(matrix)
    if len(newMatrix) > i-1 and len(newMatrix[0]) > j-1 and i >= 0 and j >= 0:
        for n in range(len(newMatrix)):
            del newMatrix[n][j-1]
        del newMatrix[i-1]
    return newMatrix

''' Тест MinorMatrix()
print(MinorMatrix(InputMatrix(int(input("Введите размер матрицы : "))), int(input("Введите номер строки : ")), int(input("Введите номер столбца : "))))
print(MinorMatrix(Matrix, 4, 4))
if MinorMatrix(Matrix, 4, 4) == [[1, 2, 3], [-1, -2, -3], [0, 1, 1]]:
    print("All right")
else:
    print("Error")
'''

def Det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for n in range(len(matrix)):
        det += (-1) ** n * matrix[0][n] * Det(MinorMatrix(matrix, 1, n+1))
    return det

''' Тест Det()
print(Det(Matrix))
if Det(Matrix) == 0:
    print("All right")
else:
    print("Error")
'''

print(Det(InputMatrix(int(input("Введите размер матрицы : ")))))
