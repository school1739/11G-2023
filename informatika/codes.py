#задание 2
'''from itertools import *

def f(x, y, z, w):
    return not(y <= x) or (z <= w) or not z


for a in product([0, 1], repeat=7):
    table = [(a[0], 0, a[1], a[2]),
             (0, 1, a[3], a[4]),
             (1, a[5], a[6], 0)]
    if len(table)== len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r)))for r in table]==[0, 0, 0]:
                print(p)'''
#задание 12
'''s='1' + '8'*80
while '18' in s or '288' in s or '3888' in s:
    if '18' in s:
        s=s.replace('18', '2', 1)
    elif '288' in s:
        s=s.replace('288', '3', 1)
    else:
        s=s.replace('3888', '1', 1)
print(s)'''

#48465 (задние 17)
'''a = [int(x) for x in open('17.txt')]
min6 = 10001
for i in range(len(a)):
    if abs(a[i]) % 10 == 6:
        min6 = min(min6, a[i])
ans = []
for i in range(len(a)-1):
    if (abs(a[i]) % 10 == 6 and abs(a[i+1]) % 10 != 6 or abs(a[i]) % 10 != 6 and abs(a[i+1]) % 10 == 6) and (a[i]**2 + a[i+1]**2 < min6**2):
        ans.append(a[i]**2 + a[i+1]**2)
print(len(ans), max(ans))'''

