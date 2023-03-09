'''the_matrix = []
str1 = []
x = int(input('Длина: '))
y= int(input('Ширина: '))
if x != y:
    print('Попробуй ещё раз, даун')
else:
    for role in range(y):
        the_matrix.append(str1)
    for kole in range(x):
        str1.append(int(input()))
print(the_matrix)'''
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def minor(a):
     b0 = a[0].pop(0)
     b1 = a[1].pop(1)
     b2 = a[2].pop(2)
     b3 = a[3].pop(3)
