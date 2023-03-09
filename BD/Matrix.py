'''the_matrix=[]
str1 = []
x = int(input())
y = int(input())
if x!=y:
    print("-")
else:
    for rol in range(y):
        the_matrix.append(str1)
    for kola in range(x):
        str1.append(int(input()))

print(the_matrix)'''

A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
def minor():
    b = A[0].pop(0)
    b1 = A[1].pop(0)
    b2 = A[2].pop(0)
    b3 = A[3].pop(0)
    print(A)



print(A)
minor()

