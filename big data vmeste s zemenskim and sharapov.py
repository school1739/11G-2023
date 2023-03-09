
'''the_matrix = []
str = []
x = int(input())
y = int(input())
if x != y:
    print('-')
else:
    for i in range(y):
        the_matrix.append([str])
    for j in range(x):
        str.append(int(input()))

print(the_matrix)'''

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
def minor(a):
    b0 = a[0].pop(0)
    b1 = a[1].pop(0)
    b2 = a[2].pop(0)
    b3 = a[0].pop(0)



