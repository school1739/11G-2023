'''
Program for calculating roots of quadratic equation
'''
'''
Calculation of discriminant
'''
def calculate_discriminant(a,b,c):
    '''
    Calculation of discriminant

    This function is calculating discriminant using the quadratic equation arguments

    Arguments:
        a -- coefficient of x^2
        b -- coefficient of x^2
        c -- constant
    returns:
        discriminant
    '''
    return b**2-4*a*c


'''
Checking the existence (and number) and calculating the roots based on discriminant
'''
def calculate_roots(d,a,b):
    '''
    The great calculation of the roots
    As you already guessed, this is the great calculation of the roots, which,
    in the name of all goodness, is calculationg thy holy roots of the greater quadratic equation
    arguments:
        d -- discriminant
        a -- coefficient of x^2
        b --
    return: none
    '''
    if d>0:
        x1=(-b+d**0.5)/(2*a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print('x1=', x1)
        print('x2=', x2)
    elif d==0:
        x=-b/(2*a)
        print('x=', x)
    else:
        print('Нет корней')
print(calculate_roots.__doc__)
'''
input coefficients: a,b,c
coefficients--int
'''
