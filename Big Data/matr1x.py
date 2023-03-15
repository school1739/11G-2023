matrix = [[1,2,3,4],
          [-1,-2,-3,-4],
          [0,1,1,0],
          [1,0,0,1]]

x = len(matrix)
n = len(matrix[0])
new_matrix = []

for kk2 in range(x-1):
    new_matrix.append(matrix[kk2+1].remove(matrix[kk2+1][0]))

print(new_matrix)