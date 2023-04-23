'''matrix = [[2, 4, 1, 1], [0, 2, 0, 0], [2, 1, 1, 3], [4, 0, 2, 3]]
x = matrix[0][0]
y =matrix[0][0]
i = (x, y)
def f(matrix, x, y):
    temp = matrix[0].pop(0)
   # for i in range(len(matrix)):

        #matrix.remove(matrix[0][0])
       # matrix.remove(matrix[0][0])


    return matrix

print(f(matrix, 0, 0))'''

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

nul_c = 0

def minor(a, elemn_d):
    if len(a) == 1:
        return a[0][0]
    else:
        from copy import deepcopy
        minor = deepcopy(a)
        global nul_c

        for col_vo_nol in minor:
            if col_vo_nol.count(0) > minor[nul_c].count(0):
                nul_c = minor.index(col_vo_nol)
            else:
                continue


        del minor[nul_c]

        for str in minor:
            del str[elemn_d]
        main_sum = []
        two_sum = []
        schet_el = 1
        el = 0

        for repeat in range(len(minor) - 1):
            for str in minor:
                schet_el *= str[el]
                el += 1
            main_sum.append(schet_el)
            schet_el = 1
            for str in minor:
                el -= 1
                schet_el *= str[el]
            two_sum.append(schet_el)
            calc_min = sum(main_sum) - sum(two_sum)
            return calc_min


def calc_det(matrix):
    det = 0
    for i in range(len(matrix)):
        det += minor(matrix, i) * (-1) ** (i + 1 + nul_c + 1) * matrix[nul_c][i]
    return det


print(calc_det(the_matrix))


