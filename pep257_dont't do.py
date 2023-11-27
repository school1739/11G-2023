"""
Program for calculating roots of a quadratic equation
"""

"""
Enter the coefficients of the equation: a, b, c
Equation coefficients -- int
"""
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

# Calculation of discriminant
d = b ** 2 - 4 * a * c

"""
Checking the existence (and number) and calculating roots 
based on the discriminant
"""
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print("x1=", x1)
    print("x2=", x2)
elif d == 0:
    x = -b / (2 * a)
    print("x=", x)
else:
    print("Корней нет")
