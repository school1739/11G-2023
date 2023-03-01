# # #Авторы: Валавин и Зинченоко
# # RUS_ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPORSTUVWXYZ"
# # ENG_ALPH = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЬЭЮЯ"
# #
# # offset = int(input('Введите сдвиг:'))
# # message = str(input('Введите сообщение:')).upper()
# # answer = ''
# # i = 0
# #
# # while (i < len(message)):
# #     if(message[i]in RUS_ALPH):
# #         newLetter = RUS_ALPH.inde (message[i]) + offset
# #         if newLetter >= 33:
# #             newLetter = newLetter - 33
# #         answer = answer + RUS_ALPH[newLetter]
# #     elif (message[i] in ENG_ALPH):
# #         if(message[i] in ENG_ALPH):
# #             newLetter = ENG_ALPH.index(message[i]) + offset
# #             if newLetter >= 26:
# #                 newLetter = newLetter - 26
# #             answer = answer + ENG_ALPH[newLetter]
# #     else:
# #         answer = answer + message[i]
# #     i = i + 1
# # print(answer)
#
# RUS_ALPHA = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
# ENG_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# answer = ""
#
# file_to_write = open("Chesarlog.txt")
# mode_choice = input("Выберите режим работы:\n"  # Ввод режима работы
#                     "1 - шифр-е\n"
#                     "2 - дешифр-е\n"
#                     "3 - bruteforce\n")
# while mode_choice not in "123":  # Защита от дурака
#     mode_choice = input("Неверный режим работы. Попробуйте ещё раз: ")
# mode_choice = int(mode_choice)
#
# text = input("Введите текст: ").upper()  # Ввод исходного сообщения
#
#
# def iterate_text(text, mode):  # Проход по символам исходного сообщения
#     global answer  # Будем записывать ответ в глобальную переменную
#     match mode:  # Выбор режима работы
#         case "encrypt":  # Шифрование
#             op = "+ offset"
#         case "decrypt":  # Дешифрование
#             op = "- offset"
#         case "bruteforce":  # Атака перебором
#             op = "- i"
#     for letter in text:  # Проход по символам
#         if letter in RUS_ALPHA:  # Если символ - русская буква
#             answer += RUS_ALPHA[eval(
#                 "RUS_ALPHA.index(letter)" + op + "% len(RUS_ALPHA)")]  # Вычисляем индекс символа в алфавите и прибавляем сдвиг
#         elif letter in ENG_ALPHA:  # Если символ - английская буква
#             answer += ENG_ALPHA[eval(
#                 "(ENG_ALPHA.index(letter)" + op + "% len(ENG_ALPHA)")]  # Вычисляем индекс символа в алфавите и прибавляем сдвиг
#         else:
#             answer += letter  # Если символ не буква, то просто добавляем его в ответ
#
#
# match mode_choice:  # Включение режима работы, соответствующего выбранному пользователем
#     case 1:
#         offset = int(input("Введите сдвиг: "))
#         iterate_text(text, "encrypt")
#         print(answer)
#         file_to_write.write(answer)
#
#     case 2:
#         offset = int(input("Введите сдвиг: "))
#         iterate_text(text, "decrypt")
#         print(answer)
#         file_to_write.write(answer)
#
#     case 3:
#         for i in range(1, 32):
#             iterate_text(text, "bruteforce")
#             print(f"Сдвиг {i}: {answer}")
#             file_to_write.write(f"Сдвиг {i}: {answer}\n")
#             answer = ""
#
#     case _: # Защита от Валавина
#         print("Неверный режим работы")
ALPHA_RUS = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
             'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
ALPHA_ENG = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

choice = int(input('1 - Шифрование\n2 - Дешифрование\n3 - bruteforce\n'))
message = str(input('Введи свое послание путник: ')).upper()
if choice == 2 or choice == 1:
    offset = int(input('Введите сдвиг:'))


# Открываем файл на запись, кодировка UTF-8
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись


# file_to_write = open('logs.txt', 'w', encoding = 'utf-8')


def shift(message, offset):
    i = 0
    answer = ''
    while (i < len(message)):
        if (message[i] in ALPHA_RUS):
            newLetter = ALPHA_RUS.index(message[i]) + offset
            if newLetter >= 33:
                newLetter = newLetter - 33
            answer = answer + ALPHA_RUS[newLetter]
        elif (message[i] in ALPHA_ENG):
            if (message[i] in ALPHA_ENG):
                newLetter = ALPHA_ENG.index(message[i]) + offset
                if newLetter >= 26:
                    newLetter = newLetter - 26
                answer = answer + ALPHA_ENG[newLetter]
        else:
            answer = answer + message[i]
        i = i + 1
    return answer


match choice:
    case 1:
        file_to_write = open('logs.txt', 'w', encoding='utf-8')
        print(shift(message, offset))
        file_to_write.write(shift(message, offset))
    case 2:
        file_to_write = open('logs.txt', 'w', encoding='utf-8')
        print(shift(message, int('-' + str(offset))))
        file_to_write.write(shift(message, int('-' + str(offset))))
    case 3:
        file_to_write = open('logs.txt', 'a', encoding='utf-8')

        i = 0
        tempVar = ''
        while i < 32:
            i += 1
            print(f'Для сдвига {i}: {shift(message, i)}')
            tempVar = tempVar + f'Для сдвига {i}: {shift(message, i)}\n'
        file_to_write.write(tempVar)
    case _:
        file_to_write = open('logs.txt', 'w', encoding='utf-8')
        print('Вы клоун')
        file_to_write.write(
            'ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД')

file_to_write.close()

# with open('logs.txt', "rb") as file:
#     session.storbinary('filippov.txt', file)



file_to_write.close()

file_to_write = open('logs.txt', 'rb')


file_to_write.close()

