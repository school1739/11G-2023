# Базанов, Кузнецов В., Егорова
from ftplib import FTP

RUS_ALPHA = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ENG_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mode_choose = input("Введите функцию:\n"
                    "1 - Шифрование\n"
                    "2 - Дешифровка\n"
                    "3 - Bruteforce\n"
                    "4 - Загрузить файл\n"
                    "5 - Скачать файл\n"
                    "6 - Посмотреть список файлов\n"
                    "7 - Выход с сервера\n")
while mode_choose not in '1234567':
    mode_choose = input("Попробуйте ввести еще раз:")
mode_choose = int(mode_choose)
file_to_write = open("CaesarLog.txt", "w", encoding="utf-8")
answer = ''

HOST = "vh388.timeweb.ru"
PORT = 21
USER = "bormotoon_infosec"
PASSWORD = "zfyLKkD3"

ftp = FTP()
ftp.connect(HOST, PORT)
ftp.login(USER, PASSWORD)


def encrypt():
    answer = ""
    offset = int(input('Введите сдвиг: '))
    # offset = offset % len(RUS_ALPHA)
    message = input('Введите сообщение: ').upper()
    for char in message:  # Проход по каждому символу в сообщении
        # Производим сдвиг
        if char in RUS_ALPHA:
            if offset > len(RUS_ALPHA):  # Проверка на сдвиг больше ли число чем длина словаря
                n = offset // len(RUS_ALPHA)
                offset = offset - n * len(RUS_ALPHA)
            rus_char_place = RUS_ALPHA.find(char)  # Ищем индекс символа
            new_place = rus_char_place + offset  # Прибовляем к индексу сдвиг
            if new_place >= len(RUS_ALPHA):  # Проверка что новый индекс меньше конечного индекса словаря
                new_place = new_place - len(RUS_ALPHA)
        else:
            if offset > len(ENG_ALPHA):  # Проверка на сдвиг больше ли число чем длина словаря
                n = offset // len(ENG_ALPHA)
                offset = offset - n * len(ENG_ALPHA)
            eng_char_place = ENG_ALPHA.find(char)  # Ищем индекс символа
            new_place = eng_char_place + offset  # Прибовляем к индексу сдвиг
            if new_place >= len(ENG_ALPHA):  # Проверка что новый индекс меньше конечного индекса словаря
                new_place = new_place - len(ENG_ALPHA)
        if char in RUS_ALPHA:
            answer += RUS_ALPHA[new_place]
        elif char in ENG_ALPHA:
            answer += ENG_ALPHA[new_place]
        else:
            answer += char
    file_to_write.write("Шифровка:")
    file_to_write.write(message)
    file_to_write.write(" - ")
    file_to_write.write(answer)
    print(answer)


def decrypt():
    answer = ""
    offset = int(input('Введите сдвиг: '))
    # offset = offset % len(RUS_ALPHA)
    message = input('Введите сообщение: ').upper()
    for char in message:  # Проход по каждому символу в сообщении
        # Производим сдвиг
        if char in RUS_ALPHA[::-1]:
            if offset > len(RUS_ALPHA):  # Проверка на сдвиг больше ли число чем длина словаря
                n = offset // len(RUS_ALPHA)
                offset = offset - n * len(RUS_ALPHA)
            rus_char_place = RUS_ALPHA.find(char)  # Ищем индекс символа
            new_place = rus_char_place - offset  # Вычитаем из индекса сдвиг
            if new_place >= len(RUS_ALPHA):  # Проверка что новый индекс меньше конечного индекса словаря
                new_place = new_place - len(RUS_ALPHA)
        else:
            if offset > len(ENG_ALPHA):  # Проверка на сдвиг больше ли число чем длина словаря
                n = offset // len(ENG_ALPHA)
                offset = offset - n * len(ENG_ALPHA)
            eng_char_place = ENG_ALPHA.find(char)  # Ищем индекс символа
            new_place = eng_char_place - offset  # Вычитаем из индекса сдвиг
            if new_place >= len(ENG_ALPHA):  # Проверка что новый индекс меньше конечного индекса словаря
                new_place = new_place - len(ENG_ALPHA)
        if char in RUS_ALPHA:
            answer += RUS_ALPHA[new_place]
        elif char in ENG_ALPHA:
            answer += ENG_ALPHA[new_place]
        else:
            answer += char
    file_to_write.write("Дешифровка:")
    file_to_write.write(message)
    file_to_write.write(" - ")
    file_to_write.write(answer)
    print(answer)


def bruteforce(message, i):  # Проход по символам исходного сообщения
    global answer  # Будем записывать ответ в глобальную переменную
    op = "- i"
    for letter in message:  # Проход по символам
        if letter in RUS_ALPHA:  # Если символ - русская буква
            answer += RUS_ALPHA[eval(
                "RUS_ALPHA.index(letter)" + op + "% len(RUS_ALPHA)")]  # Вычисляем индекс символа в алфавите и прибавляем сдвиг
        elif letter in ENG_ALPHA:  # Если символ - английская буква
            answer += ENG_ALPHA[eval(
                "(ENG_ALPHA.index(letter))" + op + "% len(ENG_ALPHA)")]  # Вычисляем индекс символа в алфавите и прибавляем сдвиг
        else:
            answer += letter  # Если символ не буква, то просто добавляем его в ответ


def choosing():  # Проверка что выбрал пользователь
    global answer, mode_choose
    match mode_choose:
        case 1:
            encrypt()
        case 2:
            decrypt()
        case 3:
            message = input('Введите сообщение: ').upper()
            file_to_write.write(message)
            for i in range(1, 32):
                bruteforce(message, i)
                print(f"Сдвиг {i}: {answer}")
                file_to_write.write(f"{i} сдвиг:{answer}")
                file_to_write.write(", ")
                answer = ""
        case 4:
            file_name = input("Какой файл отправить?\n")
            ftp.storbinary('STOR ' + file_name, open(file_name, "rb"))  # rb - Чтение двоичного файла
        case 5:
            ftp.retrlines('LIST')
            file_name = input("Выберите файл для скачивания:")
            my_file = open(file_name, 'wb')  # wb - Запись двоичного файла
            ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)
            my_file.close()
        case 6:
            ftp.retrlines('LIST')
    mode_choose = input("Введите функцию:\n"
                        "1 - Шифрование\n"
                        "2 - Дешифровка\n"
                        "3 - Bruteforce\n"
                        "4 - Загрузить файл\n"
                        "5 - Скачать файл\n"
                        "6 - Посмотреть список файлов\n"
                        "7 - Выход с сервера\n")
    while mode_choose not in '1234567':
        mode_choose = input("Попробуйте ввести еще раз:")
    mode_choose = int(mode_choose)


while mode_choose != 7:  # Пока пользователь не выбрал выход с сервера, продолжаем возврат в меню
    choosing()
file_to_write.close()
ftp.quit()
