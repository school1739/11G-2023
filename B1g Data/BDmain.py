#  1: matrix shape input (int, squared!)+
#  2: if shape 1 or 2 --> Hardcode calculation +
#  3: def minor(a) +
#  4: def calculate_det(matrix) using minor(a)+
#  5: calculate_det(matrix)+



the_matrix = [[1, 2, 3, 4],
              [-1, -2, -3, -4],
              [0, 1, 1, 0],
              [1, 0, 0, 1]]


'''def create_matrix(size_matrix):
    the_matrix = []
    for i in range(size_matrix):
        row = []
        for j in range(size_matrix):
            cocojumbo = int(input(f"Введите {j+1}-й элемент {i+1}-й строки "))
            row.append(cocojumbo)
        the_matrix.append(row)
    print(f"Создна матрица {the_matrix}")
    return the_matrix'''


def minor(a, n, m):
    working_matrix = a.copy()
    if len(working_matrix) > 2:
        summ_main = 0
        summ_second = 0
        working_matrix.pop(n)  # удаление нужной строки
        for i in range(len(working_matrix)):   # удаление нужного элемента из строки по номеру столбика
            working_matrix[i].pop(m)
        default_len = len(working_matrix)
        for v in range(len(working_matrix)):   # добавление справа нужного количества элементов в уже обрезанную матрицу
            for l in range(len(working_matrix[v])-1):
                working_matrix[v].append(working_matrix[v][l])
        #print(working_matrix)
        for p in range(default_len):
            the_last_one_main = 1
            the_last_one_second = 1
            for main_diagonal in range(default_len):
                the_last_one_main = the_last_one_main * working_matrix[main_diagonal][main_diagonal+p]
            for second_diagonal in range(1, default_len + 1):
                the_last_one_second = the_last_one_second * working_matrix[-1*second_diagonal][second_diagonal-1+p]
            summ_main += the_last_one_main
            summ_second += the_last_one_second
            #print(the_last_one_main, summ_main)
            #print(the_last_one_second, summ_second)
        #print(summ_main-summ_second)
        return summ_main - summ_second
    elif len(working_matrix) == 2:
        return 0
    else:
        return working_matrix[0][0]



def calculate_det(matrix):
    det_matrix = 0
    for m in range(len(matrix)):
        new_matrix = matrix.copy()
        print(matrix)
        det_matrix += (-1)**(1+(m+1)) * new_matrix[0][m] * (minor(new_matrix, 0, m))
    print(f'Детермината заданной матрицы равна {det_matrix}')


'''size_matrix = int(input("Введите размер для квадратной матрицы: "))
calculate_det(create_matrix(size_matrix))
'''
calculate_det(the_matrix)

# эта тварь переписывает старый список