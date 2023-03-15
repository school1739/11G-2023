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
    global zer_ind
    del_el -= 1
    minor = a.copy()
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


def calculate_det(matrix):
    pass


print(minor(the_matrix, 1))
print(the_matrix)
