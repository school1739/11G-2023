"""
Program for calculating roots of a quadratic equation
"""


def calculate_discriminant(a, b, c):
    """Calculation of discriminant

    This function is calculating a discriminant using the quadratic equation arguments.

    Args:
        a (int): first coefficient
        b (int): second coefficient
        c (int): third coefficient
    Returns:
        int: discriminant
    """
    return b ** 2 - 4 * a * c


"""
Checking the existence (and number) and calculating roots 
based on the discriminant
"""


def calculate_roots(d, a, b):
    """The Great calculation of roots

    As you already know, this function is calculating roots of a quadratic equation,
    in the name of ALL Godness, is calculating roots of a quadratic equation.

    Args:
        d (int): discriminant
        a (int): first coefficient
        b (int): second coefficient
    Returns:
        None (because it prints)
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


print(calculate_roots.__doc__)


"""
Enter the coefficients of the equation: a, b, c
Equation coefficients -- int
"""
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

# Calculation of discriminant
calculate_discriminant(a, b, c)

calculate_roots(a, b, c)
