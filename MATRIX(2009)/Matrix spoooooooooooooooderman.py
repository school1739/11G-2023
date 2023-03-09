the_matrix=[['a11','a12','a13','a14'],
            ['a21','a22','a23','a24'],
            ['a31','a32','a33','a34'],
            ['a41','a42','a43','a44']]


def minor(input, i, j):
    output = []
    for counter in range(0, len(input)):
        output.append(input[counter])
        temp = output[counter].pop(j)

    temp = output.pop(i)

    return output
print(     'Матрица')
print('a11','a12','a13','a14')
print('a21','a22','a23','a24')
print('a31','a32','a33','a34')
print('a41','a42','a43','a44')
print("Найдем Минор")
ij=int(input('Выберете число матрицы(Пример a11) :'))
if ij == a11:
    print(minor(the_matrix, 0, 0))
elif ij == a12:
    print(minor(the_matrix, 0, 1))
