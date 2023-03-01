from ftplib import FTP

RUS_ALPHA = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ENG_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ""

file_to_write = open("CaesarLog.txt", "w", encoding="utf-8")

mode_choice = input("Выберите режим работы:\n"  # Ввод режима работы
                    "1 - шифрование\n"
                    "2 - дешифрование\n"
                    "3 - bruteforce\n"
                    "4 - Список файлов на сервере\n"
                    "5 - Отправить файл\n"
                    "6 - Скачать файл\n")
while mode_choice not in "123456":  # Защита от дурака
    mode_choice = input("Неверный режим работы. Попробуйте ещё раз: ")
mode_choice = int(mode_choice)

HOST = "vh388.timeweb.ru"
PORT = 21
USER = "bormotoon_infosec"
PASSWORD = "zfyLKkD3"
ftp = FTP()
ftp.connect(HOST, PORT)
ftp.login(USER, PASSWORD)

while mode_choice != 7:
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
                    "(ENG_ALPHA.index(letter))" + op + "% len(ENG_ALPHA)")]  # Вычисляем индекс символа в алфавите и прибавляем сдвиг
            else:
                answer += letter  # Если символ не буква, то просто добавляем его в ответ


    match mode_choice:  # Включение режима работы, соответствующего выбранному пользователем
        case 1:
            text = input("Введите текст: ").upper()  # Ввод исходного сообщения
            offset = int(input("Введите сдвиг: "))
            iterate_text(text, "encrypt")
            print(answer)
            file_to_write.write("Шифровка:")
            file_to_write.write(text)
            file_to_write.write(" - ")
            file_to_write.write(answer)
        case 2:
            text = input("Введите текст: ").upper()  # Ввод исходного сообщения
            offset = int(input("Введите сдвиг: "))
            iterate_text(text, "decrypt")
            file_to_write.write("Дешифровка:")
            file_to_write.write(text)
            file_to_write.write(" - ")
            file_to_write.write(answer)
        case 3:
            text = input("Введите текст: ").upper()  # Ввод исходного сообщения
            file_to_write.write("bruteforce:")
            file_to_write.write(text)
            file_to_write.write(" - ")
            for i in range(1, 32):
                iterate_text(text, "bruteforce")
                print(f"Сдвиг {i}: {answer}")
                file_to_write.write(f"{i} сдвиг:{answer}")
                file_to_write.write(", ")
                answer = ""
        case 4:
            ftp.retrlines('LIST')
        case 5:
            # print(open())
            file_name = input("Какой файл отправить?\n")
            ftp.storbinary('STOR ' + file_name, open(file_name, "rb"))  # rb - Чтение двоичного файла
        case 6:
            ftp = FTP()
            ftp.connect(HOST, PORT)
            ftp.login(USER, PASSWORD)
            ftp.retrlines('LIST')
            file_name = input("Выберите файл для скачивания:")
            my_file = open(file_name, 'wb')  # wb - Запись двоичного файла
            ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)
            my_file.close()
        case _:  # Защита от дурака
            print("Неверный режим работы")
    choice = input("Выйти с сервера?\n"
                   "1 - Да\n"
                   "2 - Нет\n")
    choice = int(choice)
    print(choice)
    while choice != 1 or choice != 2:
        choice = input("Цифру уже нормальную введи, придурок!\n")
    if choice == 1:
        ftp.quit()
        exit()
    elif choice == 2:
        mode_choice = input("Выберите режим работы:\n"  # Ввод режима работы
                            "1 - шифрование\n"
                            "2 - дешифрование\n"
                            "3 - bruteforce\n"
                            "4 - Список файлов на сервере\n"
                            "5 - Отправить файл\n"
                            "6 - Скачать файл\n")
        while mode_choice not in "123456":  # Защита от дурака
            mode_choice = input("Неверный режим работы. Попробуйте ещё раз: ")
        mode_choice = int(mode_choice)
    file_to_write.close()

