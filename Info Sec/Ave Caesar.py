#Базанов, Савченко, Кузнецов В.
from ftplib import FTP

RUS_ALPHA = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ENG_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ""

HOST = "vh388.timeweb.ru"
PORT = 21
USER = "bormotoon_infosec"
PASSWORD = "zfyLKkD3"
chosen = int(input("Выберите действие:\n1 - Отправить\n2 - Скачать"))
match chosen:
    case 1:
        # Отрываем файл на запись кодировка UTF - 8
        # Аргументы: имя файла, режим работы, кодировка
        # Режим работы
            # w - write (только чтение)
            # r - read (запись)
            # a - append (добавить в конец)
        file_to_write = open("CaesarLog.txt", "w", encoding="utf-8")
        file_to_append = open("CaesarLog.txt", "a", encoding="utf-8")

        mode_choice = input("Выберите режим работы:\n"  # Ввод режима работы
                            "1 - шифрование\n"
                            "2 - дешифрование\n"
                            "3 - bruteforce\n")
        while mode_choice not in "123":  # Защита от дурака
            mode_choice = input("Неверный режим работы. Попробуйте ещё раз: ")
        mode_choice = int(mode_choice)

        text = input("Введите текст: ").upper()  # Ввод исходного сообщения


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
                offset = int(input("Введите сдвиг: "))
                iterate_text(text, "encrypt")
                print(answer)
                file_to_write.write("Шифровка:")
                file_to_write.write(text)
                file_to_write.write(" - ")
                file_to_write.write(answer)
            case 2:
                offset = int(input("Введите сдвиг: "))
                iterate_text(text, "decrypt")
                file_to_write.write("Дешифровка:")
                file_to_write.write(text)
                file_to_write.write(" - ")
                file_to_write.write(answer)

            case 3:
                file_to_append.write("bruteforce:")
                file_to_append.write(f"\n{text}")
                for i in range(1, 32):
                    iterate_text(text, "bruteforce")
                    print(f"Сдвиг {i}: {answer}")
                    file_to_append.write(f"\n{i} сдвиг:{answer}")
                    file_to_append.write(", ")
                    answer = ""

            case _:  # Защита от дурака
                print("Неверный режим работы")
        file_to_write.close()
        con = FTP(HOST, USER, PASSWORD)
        con.connect()
        con.storbinary("Caesar.txt")
    case 2:
        con = FTP(HOST, USER, PASSWORD)
        con.connect()
        con.retrbinary("Caesar.txt")
    case _:
        print("Что-то не то")
