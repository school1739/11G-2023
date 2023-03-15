# TODO 1: matrix shape input (int, squared!)
# TODO 2: if shape 1 or 2 --> Hardcode calculation
# TODO 3: def minor(a)
# TODO 4: def calculate_det(matrix) using minor(a)
# TODO 5: calculate_det(matrix)

the_matrix = [[1, 2, 3, 4],
              [-1, -2, -3, -4],
              [0, 1, 1, 0],
              [1, 0, 0, 1]]
zer_ind = 0


def minor(a, del_el):
    import copy
    minor = copy.deepcopy(a)
    global zer_ind
    del_el -= 1
    # Считаем макс. кол-во нулей и запоминаем индекс
    max_zer = 0
    for count_zer in minor:
        if count_zer.count(0) > max_zer:
            max_zer = count_zer.count(0)
            zer_ind = minor.index(count_zer)
    # Удаляем строку с макс. кол-вом нулей
    del minor[zer_ind]
    # Итерируемся по строкам
    for stroke in minor:
        del stroke[del_el]
    return minor


def calculate_det():
    pass
    det = the_matrix[zer_ind][0] * minor(the_matrix, 1) * -1 ** (1 + zer_ind + 1) + \
          -1 ** (2 + zer_ind + 1) * the_matrix[zer_ind][1] * minor(the_matrix, 2) + \
          -1 ** (3 + zer_ind + 1) * the_matrix[zer_ind][2] * minor(the_matrix, 3) + \
          -1 ** (4 + zer_ind + 1) * the_matrix[zer_ind][3] * minor(the_matrix, 4)
    return det


print(minor(the_matrix, 1))
print(the_matrix)
