#создание матрицы(можно выбирать размер)
the_matrix=[]
p = 0
size = 3 #int(input(f"размер матрицы: "))
for x in range(size):
    spx=[]
    for sp in range(size):
        p += 1
        k = int(input(f"значение {p}: "))
        spx.append(k)
    the_matrix.append(spx)





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
    print(minor)
    print(minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0])
    el = 0
    a = 1
    for repeat in range(len(minor)):
        for stroke in minor:
            a *= stroke[el]
            if el == len(stroke):
                el = 0
            else:
                el += 1
    return minor