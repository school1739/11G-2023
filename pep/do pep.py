"""
Program for calculating roots of a quadratic equation
"""
"""
Calculate the discriminant
"""
def calculate_discriminant(a,b,c):
    """Calculate the discriminant

    This function is calculating a discriminant using the quadratic equation arguments

    Arguments:
        a-- coefficient of x^2
        b-- coefficient of x
        c-- constant
    returns:
        discriminant

    """
    return b**2-4*a*c


'''
Checking the presence and calculation of roots on the basis of discriminant
'''
def calculate_roots(d,a,b):
    """The greate colculating roots
    This function is culculating roots of quadratic roots

    arguments:
        d--discriminant
        a--coafficient of x^2
        b--coafficient of x
    return: none

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
print(calculate_roots.__doc__)
'''
Input coefficients: a,b,c
Coefficients--int
'''
