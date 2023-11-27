"""
enter the conefficients
""" 
a = float(input())
b = float(input())
c = float(input())

def GetDiscriminant(a, b, c):
"""
Calculates discriminant

Arguments :
a - x^2 coefficient
b - x coefficient
c - constant

Returns :
real discriminant
"""
    return b ** 2 - 4 * a * c

def GetRootsOfQuadraticEquation(a, b, c):
"""
Calculates roots of an equation

Arguments :
a - x^2 coefficient
b - x coefficient
c - constant

Returns :
list of real roots
"""
    d = GetDiscriminant(a, b, c)
    if d > 0:
        x1 = (-b - d ** 0.5) / (2 * a)
        x2 = (-b + d ** 0.5) / (2 * a)
        return [x1, x2]
    elif d == 0:
        x = (-b) / (2 * a)
        return [x]
    else:
        return []

"""
Print roots of an equation
"""
print(SolveQuadraticEquation(a, b, c))
