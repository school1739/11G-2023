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
s='1' + '8'*80
while '18' in s or '288' in s or '3888' in s:
    if '18' in s:
        s=s.replace('18', '2', 1)
    elif '288' in s:
        s=s.replace('288', '3', 1)
    else:
        s=s.replace('3888', '1', 1)
print(s)
