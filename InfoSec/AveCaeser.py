from ftplib import FTP
Host = "vh.388.timeweb.ru"
Port = 21
User = "bormotoon_infosec"
Password = "zfyLKkD3"
client = FTP(Host, User, Password)
client.encoding = "utf-8"
Alphabet_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
Alphabet_EN = "ABCDEFGHIKLMNOPQRSTVXYZ"
#filename = "CaeserLog.txt"

#with open(filename, "rb") as file:
#    client.storbinary(f"STOR {filename}", file)

#with open(filename, "rb") as file:
#    client.retrbinary(f"STOR {filename}", file)
#fileToWrite = open("CaeserLog.txt", "a", encoding="utf-8")
#имя, режим работы, кодировка
#r - read
#w - write
#a - append

def main():
    while True:
        message = input("Введите сообщение : ").upper()
        if message == "":
            break
        print("Encrypt - 1")
        print("Decrypt - 2")
        print("Brute force - 3")
        choice = int(input("Выберите режим : "))
        match choice:
            case 1:
                fileToWrite.write(f"\nencrypt {encrypt(message, int(input('Сдвиг : ')))} \n")
            case 2:
                fileToWrite.write(f"\ndecrypt {decrypt(message, int(input('Сдвиг : ')))} \n")
            case 3:
                bruteforce(message)
            case _:
                print("Ошибка ввода")

def encrypt(message, offset):
    answer = ""
    for char in message:
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
    fileToWrite.write(f"\nbruteforce {message}: \n")
    for i in range(len(Alphabet_RU)):
        fileToWrite.write(f"{i} : {encrypt(message, i)}\n")

main()