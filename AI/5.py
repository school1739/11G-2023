'''for n in range (1,100):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s += '00'
    else:
        s += '10'
    r = int(s,2)
    if r>43:
        print(r)
        break'''

'''def f(s):
    summa = 0
    for i in range(len(s)):
        summa += int(s[i])
    return summa
for n in range(1, 100):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = str(s)
    summa = f(s)
    s = s + str(summa % 2)
    summa = f(s)
    s = s + str(summa % 2)
    r = int(s, 2)  # перевод в десятичную систему
    if r > 97:
        print(r)
        break'''

'''for n in range(1, 100):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = str(s)
    if s.count('1') % 2 == 0: 
        s += '1'
    else:
        s += '0'
    if s.count('1') % 2 == 0:
        s += '1'
    elif s.count('1') % 2 == 1:
        s += '0'
    r = int(s, 2)  # перевод в десятичную систему
    if r > 54:
        print(r)
        break'''