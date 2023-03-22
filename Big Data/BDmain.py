# TODO 2: if shape 1 or 2 --> Hardcode calculation
# TODO 3: def minor(a)
# TODO 4: def calculate_det(matrix) using minor(a)
# TODO 5: calculate_det(matrix)

a11 = int(input())
a12 = int(input())
a13 = int(input())
a21 = int(input())
a22 = int(input())
a23 = int(input())
a31 = int(input())
a32 = int(input())
a33 = int(input())
the_matrix = [[a11, a12, a13],
              [a21, a22, a23],
              [a31, a32, a33]]

zer_ind = 0  # Переменная для сохранения индекса строки с макс. кол-вом нулей


def minor(a, del_el):
    from copy import deepcopy
    minor = deepcopy(a)  # Создаем независимую копию матрицы
    global zer_ind
    # Запоминаем индекс строки с макс. кол-вом нулей
    for count_zer in minor:
        if count_zer.count(0) > minor[zer_ind].count(0):
            zer_ind = minor.index(count_zer)
        else:
            continue
    # Удаляем строку с макс. кол-вом нулей
    del minor[zer_ind]
    # Итерируемся по строкам
    for stroke in minor:
        del stroke[del_el]  # Удаляем элемент нужного столбца в каждой строке
    # Вычисление полученного минора
    v = []
    calc_el = 1
    el = 0
    for repeat in range(len(minor) - 1):  # Считаем количество повторов для минора
        for stroke in minor:
            calc_el *= stroke[el]  # Перемножаем каждый элемент строки смещаясь на один вправо
            print(stroke[el])
            el += 1
        v.append(calc_el)
        calc_el = 1
        for stroke in minor:  # Перемножаем каждый элемент строки смещаясь на один влево
            el -= 1
            print(stroke[el])
            calc_el *= stroke[el]
        calc_min = v[0] - calc_el
        return calc_min


print(minor(the_matrix, 0))
