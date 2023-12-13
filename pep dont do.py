'''
Program for calculating roots of a quadratic equation
'''

'''
Input coefficients: a,b,c
Coefficients--int
'''
a=int(input("введите А:"))
b=int(input("введите B:"))
c=int(input("введите C:"))

# Вычисление дискриминанта
d=b**2-4*a*c

"""
Checking the presence and calculation of roots on the basis of discriminant
"""
if d>0:
    x1=(-b+d**0.5)/(2*a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(x1)
    print(x2)
elif d==0:
    x=-b/(2*a)
    print(x)
else:
    print("нет корней")