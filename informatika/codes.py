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


# Поляков 5066
'''a = [int(x) for x in open('17-288.txt')]
ans = []
for i in range(len(a)-2):
    if abs(a[i]) % 7 != abs(a[i+1]) % 7 and abs(a[i+1]) % 7 != abs(a[i+2]) % 7 and abs(a[i]) % 7 != abs(a[i+2]) % 7 and (a[i] < 0 or a[i+1] < 0 or a[i+2] < 0):
        ans.append(max(a[i], a[i+1], a[i+2]) - min(a[i], a[i+1], a[i+2]))
print(len(ans), min(ans))'''

#задание 16 поляков 224
'''def f(n):
    if n == 1: return 1
    if n > 1 and n % 2 == 0: return n*n + f(n-1)
    if n > 1 and n % 2 != 0: return f(n-1)+ 2 * f(n-2)


print(f(23)'''
'''from sys import *
setrecursionlimit(10000)


def f(n):
    if n == 1: return 1
    if n > 1: return n * f(n-1)

print(f(2023)/f(2020))'''
# 2021 * 2022 * 2023

'''def f(n):
    if n >= 2025: return n
    if n < 2025: return n + f(n+2)

print(f(2022)-f(2023))'''

# поляков 2265
'''def f(n):
    if n <= 3: return n
    if 3 < n <= 32: return n // 4 + f(n - 3)
    if n > 32: return 2 * f(n - 5)def f(n - 5)


print(f(100))'''
# Поляков 2278
'''k=0
def f(n):
    if n > 25: return 2*n*n*n + 1
    if n <= 25: return f(n+2) + 2*f(n+3)


for n in range(1, 1001):
    if f(n)%11==0:
        k+=1

print(k)'''


'''def f(n):
    if n <= 1: return 1
    if n > 1 and n % 2 == 0: return  3 + f(n / 2 - 1)
    if n > 1 and n % 2 != 0: return n + f(n + 2)
n = 2
while n < 1000:
    try:
        r = f(n)
        if r == 19:
            print(n)
            break
    except:
        pass
    n += 1'''

# кегэ 2686
f = open('26_2686.txt')
k = int(f.readline())
a = sorted([list(map(int, x.split())) for x in f])
count = 0
for i in range(k-1):
    if a[i][0] == a[i + 1][0] and a[i][1] + 1 == a[i+1][1]:
        count += 1
        if count >= 5:
            print(a[i][0], a[i][1] + 1)
    else:
        count = 0
