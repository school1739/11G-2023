from ftplib import FTP

Alphabet_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
Alphabet_EN = "ABCDEFGHIKLMNOPQRSTVXYZ"

HOST = 'vh388.timeweb.ru'
PORT = 21
USER = 'bormotoon_infosec'
PASSWORD = 'zfyLKkD3'

ftp_server = FTP(HOST, USER, PASSWORD)
filename = "CaesarLog.txt"

with open(filename, "rb") as file:
    ftp_server.storbinary(f"STOR {filename}", file)

with open(filename, "wb") as file:
    ftp_server.retrbinary(f"RETR {filename}", file.write)

file = open(filename, "r")
print('File Content:', file.read())
ftp_server.quit()
#Открываем файл на запись кодировка utf-8
#аргументы: имя файла, режим работы, кодировка
#Режим работы:
    #r-read(только чтение)
    #w-write(только запись)
    #a-append(добавл в конец)
fileToWrite=open("CaesarLog.txt", "w", encoding="utf-8")
def main():
    message = input("Введите сообщение : ").upper()
    print("Encrypt - 1")
    print("Decrypt - 2")
    print("Brute force - 3")
    choice = int(input("Выберите режим : "))
    match choice:
        case 1:
            encrypt(message, int(input("Сдвиг : ")))
        case 2:
            decrypt(message, int(input("Сдвиг : ")))
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
    print(answer)
def decrypt(message, offset):
    answer = ""
    for char in message:
        if char in Alphabet_RU:
            answer += Alphabet_RU[(Alphabet_RU.find(char) - offset) % len(Alphabet_RU)]
        elif char in Alphabet_EN:
            answer += Alphabet_EN[(Alphabet_EN.find(char) - offset) % len(Alphabet_EN)]
        else:
            answer += char
    print(answer)
def bruteforce(message):
    for i in range(len(Alphabet_RU)):
        encrypt(message, i)
main()

