Alphabet_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
Alphabet_EN = "ABCDEFGHIKLMNOPQRSTVXYZ"
fileToWrite=open("CaesarLog.txt", "w", encoding="utf-8")
def main():
    message = input("Введите сообщение : ").upper()
    print("Encrypt - 1")
    print("Decrypt - 2")
    print("Brute force - 3")
    choice = int(input("Выберите режим : "))
    match choice:
        case 1:
            print(encrypt(message, int(input("Сдвиг : "))))
        case 2:
            print(decrypt(message, int(input("Сдвиг : "))))
        case 3:
            bruteforce(message)
        case _:
            print("Ошибка ввода")
def encrypt(message, offset):
    answer = ""    for char in message:
        if char in Alphabet_RU:
            answer += Alphabet_RU[(Alphabet_RU.find(char) + offset) % len(Alphabet_RU)]
        elif char in Alphabet_EN:
            answer += Alphabet_EN[(Alphabet_EN.find(char) + offset) % len(Alphabet_EN)]
        else:
            answer += char
    return answer
def decrypt(message, offset):
    answer = ""
    for char in message:
        if char in Alphabet_RU:
            answer += Alphabet_RU[(Alphabet_RU.find(char) - offset) % len(Alphabet_RU)]
        elif char in Alphabet_EN:
            answer += Alphabet_EN[(Alphabet_EN.find(char) - offset) % len(Alphabet_EN)]
        else:
            answer += char
    return answer
def bruteforce(message):
    for i in range(len(Alphabet_RU)):
        fileToWrite.write(f"{i}: {encrypt(message, i)}\n")
main()

