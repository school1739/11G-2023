'''from fnmatch import *

for x in range(0, 10**10+1, 2024):
    if fnmatch(str(x), '1?2157*4'):
        print(x, x//2024)'''

'''x = int(input())
d = []
for i in range(1, x + 1):
    if x % i == 0:
        d.append(i)
print(d)'''

'''def div(x):    #div = f
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)'''
#2562 полякв
'''def div(x):    #div = f
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(174457, 174505+1):
    if len(div(x))==2:
        print(div(x))'''

#2572 поляков
'''def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            if i%2==0:
                d.add(i)
            if (x//i)%2==0:
                d.add(x//i)
    return sorted(d)


for x in range(190201, 190260+1):
    if len(div(x))==4:
        print(div(x)[-1], div(x)[-2])'''

