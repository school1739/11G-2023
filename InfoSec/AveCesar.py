RUS_ALPHA = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ENG_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ""

# Открыть файл
file_to_write = open("CesarLog.txt", "w", encoding = "utf-8") # w - писать, r - читать

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
                "(ENG_ALPHA.index(letter)" + op + "% len(ENG_ALPHA)")]  # Вычисляем индекс символа в алфавите и прибавляем сдвиг
        else:
            answer += letter  # Если символ не буква, то просто добавляем его в ответ


match mode_choice:  # Включение режима работы, соответствующего выбранному пользователем
    case 1:
        offset = int(input("Введите сдвиг: "))
        iterate_text(text, "encrypt")
        print(answer)
        file_to_write.write(answer) # Записать в файл

    case 2:
        offset = int(input("Введите сдвиг: "))
        iterate_text(text, "decrypt")
        print(answer)
        file_to_write.write(answer) # Записать в файл

    case 3:
        for i in range(1, 32):
            iterate_text(text, "bruteforce")
            print(f"Сдвиг {i}: {answer}")
            file_to_write.write(f"Сдвиг {i}: {answer}\n") # Записать в файл
            answer = ""


    case _: # Защита от дурака
        print("Неверный режим работы")

file_to_write.close() # Закрыть файл
