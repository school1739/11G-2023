a11 = int(input())
a12 = int(input())
a13 = int(input())
a14 = int(input())
a21 = int(input())
a22 = int(input())
a23 = int(input())
a24 = int(input())
a31 = int(input())
a32 = int(input())
a33 = int(input())
a34 = int(input())
a41 = int(input())
a42 = int(input())
a43 = int(input())
a44 = int(input())
the_matrix = [[a11, a12, a13, a14],
              [a21, a22, a23, a24],
              [a31, a32, a33, a34],
              [a41, a42, a43, a44]]

zer_ind = 0  # Переменная для сохранения индекса строки с макс. кол-вом нулей


def minor(a, del_el):
    if len(a) == 1:
        return a[0][0]
    else:
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
        main_sum = []
        vtor_sum = []
        calc_el = 1
        el = 0
        for repeat in range(len(minor) - 1):  # Считаем количество повторов для минора
            for stroke in minor:
                calc_el *= stroke[el]  # Перемножаем каждый элемент строки смещаясь на один вправо
                el += 1
            main_sum.append(calc_el)
            calc_el = 1
            for stroke in minor:  # Перемножаем каждый элемент строки смещаясь на один влево
                el -= 1
                calc_el *= stroke[el]
            vtor_sum.append(calc_el)
            calc_min = sum(main_sum) - sum(vtor_sum)
            return calc_min


def calc_det(matrix):
    det = 0
    for i in range(len(matrix)):
        det += minor(matrix, i) * (-1) ** (i + 1 + zer_ind + 1) * matrix[zer_ind][i]
    return det


print(calc_det(the_matrix))

# Ну вроде считает, вопрос только правильно ли...