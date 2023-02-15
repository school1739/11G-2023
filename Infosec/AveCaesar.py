from ftplib import FTP
RUS_ALPHA = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ENG_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

HOST = "vh388.timeweb.ru"
PORT = 21
USER = "bormotoon_infosec"
PASSWORD = "zfyLKkD3"

ftp = FTP()
ftp.connect(HOST, PORT)
ftp.login(USER, PASSWORD)

# Открываем файл на запись, кодировка utf-8
# аргументы: имя файла, режим работы, кодировка
# Режимы работы
    # r - read (только чтение)
    # w -write (запись)
    # a - append (добавить в конец)

mode = int(input('Введите режим: '))
while str(mode) not in '123':
    mode = int(input())

ftp_mode = int(input('Введите режим FTP: '))
while str(mode) not in '12':
    mode = int(input())


message = input('Введите сообщение: ').upper()
offset = int(input('Введите сдвиг: '))
def encrypt(offset, message, k, updo): # k=1, если используется в брутфорсе
    offset = int(offset)
    offset = offset % len(RUS_ALPHA)
    answer = ''
    for char in message:
        if char in RUS_ALPHA:
            char_place = RUS_ALPHA.find(char)
            new_place = char_place + offset
            if char in RUS_ALPHA:
                answer += RUS_ALPHA[new_place % len(RUS_ALPHA)]
        elif char in ENG_ALPHA:
            char_place = ENG_ALPHA.find(char)
            new_place = char_place + offset
            if char in ENG_ALPHA:
                answer += ENG_ALPHA[new_place % len(ENG_ALPHA)]
        else:
            answer += char

    a = f'Сдвиг {offset}: {answer}\n'
    print(f'Сдвиг {offset}: {answer}')
    if k == 1 and updo == 1:
        file_to_write = open("CaesarBebra.txt", "a", encoding='utf-8')
        file_to_write.write(a) # Добавить в файл
        ftp.storbinary(f"STOR CaesarBebra.txt", file_to_write)
    elif updo == 2:
        file_to_write = open("CaesarBebra.txt", "w", encoding='utf-8')
        file_to_write.write(a)  # Запись в файл
        ftp.storbinary(f"STOR CaesarBebra.txt", file_to_write)

def decrypt(offset, message):
    offset = int(offset)
    offset = offset % len(RUS_ALPHA)

    answer = ''
    for char in message:
        if char in RUS_ALPHA:
            char_place = RUS_ALPHA.find(char)
            new_place = char_place - offset
            if char in RUS_ALPHA:
                answer += RUS_ALPHA[new_place % len(RUS_ALPHA)]
        elif char in ENG_ALPHA:
            char_place = ENG_ALPHA.find(char)
            new_place = char_place - offset
            if char in ENG_ALPHA:
                answer += ENG_ALPHA[new_place % len(ENG_ALPHA)]
        else:
            answer += char
    print(answer)
    file_to_write = open("CaesarBebra.txt", "w", encoding='utf-8')
    file_to_write.write(answer)  # Запись в файл
    file_to_write.close()

def bruteforce(message):
    for i in range(1, 32):
        encrypt(i, message, 1)


match mode:
     case 1:
         encrypt(offset, message, 0)
         match ftp_mode:
             case 1:
                encrypt(offset, message, 0, 'up')
             case 2:
                encrypt(offset, message, 0, 'do')
     case 2:
         decrypt(offset, message)
         match ftp_mode:
             case 1:
                 encrypt(offset, message, 0, 'up')
             case 2:
                 encrypt(offset, message, 0, 'do')
     case 3:
         bruteforce(message)
         match ftp_mode:
             case 1:
                 encrypt(offset, message, 0, 'up')
             case 2:
                 encrypt(offset, message, 0, 'do')
     case _:
         print("Нет такого режима")

