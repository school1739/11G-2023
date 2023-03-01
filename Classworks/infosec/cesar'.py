from ftplib import FTP

# Алфавиты для шифрования
RUS_ALPHA = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ENG_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Переменная для записи ответа
answer = ""

# FTP credentials
HOST = "HOST"
PORT = 21
USER = "USER"
PASSWORD = "PASSWORD"


def iterate_text(text, mode):  # Проход по символам исходного сообщения
    global answer  # Будем записывать ответ в глобальную переменную
    match mode:  # Выбор режима работы
        case "encrypt":  # Шифрование
            op = "+ offset"
        case "decrypt":  # Дешифрование
            op = "- offset"
        case "bruteforce":  # Атака перебором
            op = "- i"
    for letter in text:  # Проход по символам
        if letter in RUS_ALPHA:  # Если символ - русская буква
            answer += RUS_ALPHA[eval(
                "RUS_ALPHA.index(letter)" + op + "% len(RUS_ALPHA)")]  # Вычисляем индекс символа в алфавите и прибавляем сдвиг
        elif letter in ENG_ALPHA:  # Если символ - английская буква
            answer += ENG_ALPHA[eval(
                "ENG_ALPHA.index(letter)" + op + "% len(ENG_ALPHA)")]  # Вычисляем индекс символа в алфавите и прибавляем сдвиг
        else:
            answer += letter  # Если символ не буква, то просто добавляем его в ответ


# Создаём соединение с FTP-сервером
srv = FTP()
srv.connect(HOST, PORT)
srv.login(USER, PASSWORD)

# Отрываем файл на запись, кодировка UTF-8
# Аргументы: имя файла, режим работы, кодировка
# Режимы работы:
# r - read (только чтение)
# w - write (запись)
# a - append (добавить в конец)
# file_to_write = open("CaesarLog.txt", "w", encoding="utf-8")

coding_mode_choice = input("Выберите режим работы:\n"  # Ввод режима работы
                           "1 - шифрование\n"
                           "2 - дешифрование\n"
                           "3 - bruteforce\n")
while coding_mode_choice not in "123":  # Защита от дурака
    coding_mode_choice = input("Неверный режим работы. Попробуйте ещё раз: ")
coding_mode_choice = int(coding_mode_choice)

text = input("Введите текст: ").upper()  # Ввод исходного сообщения

match coding_mode_choice:  # Включение режима работы, соответствующего выбранному пользователем
    case 1:
        offset = int(input("Введите сдвиг: "))
        iterate_text(text, "encrypt")
        print(answer)
        the_file = open("CaesarLog.txt", "w", encoding="utf-8")
        the_file.write(answer)  # Запись в файл

    case 2:
        offset = int(input("Введите сдвиг: "))
        iterate_text(text, "decrypt")
        print(answer)
        the_file = open("CaesarLog.txt", "w", encoding="utf-8")
        the_file.write(answer)  # Запись в файл

    case 3:
        for i in range(1, 32):
            iterate_text(text, "bruteforce")
            print(f"Сдвиг {i}: {answer}")
            the_file = open("CaesarLog.txt", "a", encoding="utf-8")
            the_file.write(f"Сдвиг {i}: {answer}\n")  # Запись в файл
            answer = ""

    case _:  # Защита от дурака
        print("Неверный режим работы")  # Вывод сообщения об ошибке

ftp_mode_choice = input("Выберите режим работы с FTP-сервером:\n"  # Ввод режима работы
                        "1 - Получить список файлов на сервере\n"
                        "2 - Загрузить файл на сервер\n"
                        "3 - Скачать файл с сервера\n"
                        "4 - Выход\n")
while ftp_mode_choice not in "1234":  # Защита от дурака
    ftp_mode_choice = input("Неверный режим работы. Попробуйте ещё раз: ")
ftp_mode_choice = int(ftp_mode_choice)

match ftp_mode_choice:  # Включение режима работы, соответствующего выбранному пользователем
    case 1:  # Получение списка файлов на FTP-сервере
        dir_list = srv.nlst()
        for filename in dir_list:
            print(filename, end="\n")

    case 2:  # Загрузка файла на FTP-сервер
        file_to_upload = input("Введите имя файла для загрузки: ")
        srv.storbinary('STOR ' + file_to_upload, open(file_to_upload, 'rb'))

    case 3:  # Скачивание файла с FTP-сервера
        dir_list = srv.nlst()
        for filename in dir_list:
            print(filename, end="\n")
        file_to_download = input("Введите имя файла для скачивания: ")
        while file_to_download not in dir_list:  # Защита от дурака
            file_to_download = input("Неверное имя файла. Попробуйте ещё раз: ")
        with open(file_to_download, 'wb') as df:
            srv.retrbinary('RETR ' + file_to_download, df.write)
    case 4:  # Выход
        srv.quit()
        exit()

    case _:  # Защита от дурака
        print("Неверный режим работы")  # Вывод сообщения об ошибке

the_file.close()  # Закрытие файла