import random
import os


def generate_prime_number():
    prime_number = random.randint(100, 1000)
    while not is_prime(prime_number):
        prime_number += 1
    return prime_number


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_keys():
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e += 1
    d = pow(e, -1, phi)

    with open("public_key.txt", "w") as file:
        file.write(f"{e} {n}")

    with open("private_key.txt", "w") as file:
        file.write(f"{d} {n}")

    print("Keys generated successfully!")


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def encrypt_text():
    with open("public_key.txt", "r") as file:
        e, n = map(int, file.readline().split())

    with open("plaintext.txt", "r") as file:
        plaintext = file.read()

    symmetric_key = random.randint(1, 256)
    encrypted_key = pow(symmetric_key, e, n)

    with open("encrypted_key.txt", "w") as file:
        file.write(str(encrypted_key))

    encrypted_text = ""
    for char in plaintext:
        encrypted_char = ord(char) ^ symmetric_key
        encrypted_text += hex(encrypted_char)[2:].zfill(2)

    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

    print("Text encrypted successfully!")


def decrypt_text():
    with open("private_key.txt", "r") as file:
        d, n = map(int, file.readline().split())

    with open("encrypted_key.txt", "r") as file:
        encrypted_key = int(file.read())

    symmetric_key = pow(encrypted_key, d, n)

    with open("encrypted_text.txt", "r") as file:
        encrypted_text = file.read()

    plaintext = ""
    for i in range(0, len(encrypted_text), 2):
        encrypted_char = int(encrypted_text[i:i + 2], 16)
        decrypted_char = encrypted_char ^ symmetric_key
        plaintext += chr(decrypted_char)

    with open("decrypted_text.txt", "w") as file:
        file.write(plaintext)

    print("Text decrypted successfully!")


print("1. Generate keys")
print("2. Encrypt text")
print("3. Decrypt text")

choice = input("Enter your choice: ")

if choice == "1":
    generate_keys()
elif choice == "2":
    encrypt_text()
elif choice == "3":
    decrypt_text()
else:
    print("Invalid choice")