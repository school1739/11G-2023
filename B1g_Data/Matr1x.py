matrix = [[1, 2, 3, 4],
          [-1, -2, -3, -4],
          [0, 1, 1, 0],
          [1, 0, 0, 1]]
print(matrix[1][2])


def minor(a):
    # Определитель кол-ва нулей
    # zeros = {1:[],
    #          2:[],
    #          3:[],
    #          4:[]}
    # for i in matrix:
    #     print(i, end=' ')
    #     print(zeros)
    #     for j in i:
    #         if j == 0:
    #             zeros += 1
    #         else:
    #             continue
    minor = matrix.pop(matrix[1][1])

    return minor


print(minor(matrix))
