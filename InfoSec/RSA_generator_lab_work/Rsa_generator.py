import random


def generate_rsa_keys():
    # Генерация двух простых чисел p и q
    p = generate_prime_number()
    q = generate_prime_number()

    # Вычислить n = p * q
    n = p * q

    # Вычислить функцию Эйлера phi(n)
    phi_n = (p - 1) * (q - 1)

    # Выбор публичной экспоненты e
    e = choose_public_exponent(phi_n)

    # Вычислить частную экспоненту d
    d = compute_private_exponent(e, phi_n)

    # Хранить открытый ключ (e, n) в файле
    store_public_key(e, n)

    # Хранить закрытый ключ (d, n) в другом файле
    store_private_key(d, n)


def generate_prime_number():
    # Сгенерировать случайное число и проверить, является ли оно простым
    while True:
        num = random.randint(2, 1000)
        if is_prime(num):
            return num


def is_prime(num):
    # Проверить, является ли число простым
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def choose_public_exponent(phi_n):
    # Выберите публичную экспоненту e такую, что 1 < e < phi(n) и gcd(e, phi(n)) = 1
    while True:
        e = random.randint(2, phi_n - 1)
        if gcd(e, phi_n) == 1:
            return e


def gcd(a, b):
    # Вычислить наибольший общий делитель двух чисел
    while b != 0:
        a, b = b, a % b
    return a


def compute_private_exponent(e, phi_n):
    # Вычислить частную экспоненту d такую, что d * e ≡ 1 (mod phi(n))
    d = extended_euclidean_algorithm(e, phi_n)
    return d


def extended_euclidean_algorithm(a, b):
    # Вычислить частную экспоненту d по расширенному евклидову алгоритму
    if b == 0:
        return 1, 0
    else:
        x, y = extended_euclidean_algorithm(b, a % b)
        return y, x - (a // b) * y


def store_public_key(e, n):
    # Хранить открытый ключ (e, n) в файле
    with open('public_key.txt', 'w') as file:
        file.write(f"Public Key (e, n): ({e}, {n})")


def store_private_key(d, n):
    # Хранить закрытый ключ (d, n) в файле
    with open('private_key.txt', 'w') as file:
        file.write(f"Private Key (d, n): ({d}, {n})")


generate_rsa_keys()