# ALPHA_RUS = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
#              'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
# ALPHA_ENG = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
#              'V', 'W', 'X', 'Y', 'Z']

# choice = int(input('1 - Шифрование\n2 - Дешифрование\n3 - хз\n'))
# message = str(input('ТЕКСT: ')).upper()
# if choice == 2 or choice == 1:
#     offset = int(input('Введите сдвиг:'))


# # Открываем файл на запись, кодировка UTF-8
# # 'r'	открытие на чтение (является значением по умолчанию).
# # 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# # 'x'	открытие на запись, если файла не существует, иначе исключение.
# # 'a'	открытие на дозапись, информация добавляется в конец файла.
# # 'b'	открытие в двоичном режиме.
# # 't'	открытие в текстовом режиме (является значением по умолчанию).
# # '+'	открытие на чтение и запись


# # file_to_write = open('logs.txt', 'w', encoding = 'utf-8')


# def shift(message, offset):
#     i = 0
#     answer = ''
#     while (i < len(message)):
#         if (message[i] in ALPHA_RUS):
#             newLetter = ALPHA_RUS.index(message[i]) + offset
#             if newLetter >= 33:
#                 newLetter = newLetter - 33
#             answer = answer + ALPHA_RUS[newLetter]
#         elif (message[i] in ALPHA_ENG):
#             if (message[i] in ALPHA_ENG):
#                 newLetter = ALPHA_ENG.index(message[i]) + offset
#                 if newLetter >= 26:
#                     newLetter = newLetter - 26
#                 answer = answer + ALPHA_ENG[newLetter]
#         else:
#             answer = answer + message[i]
#         i = i + 1
#     return answer


# match choice:
#     case 1:
#         file_to_write = open('logs.txt', 'w', encoding='utf-8')
#         print(shift(message, offset))
#         file_to_write.write(shift(message, offset))
#     case 2:
#         file_to_write = open('logs.txt', 'w', encoding='utf-8')
#         print(shift(message, int('-' + str(offset))))
#         file_to_write.write(shift(message, int('-' + str(offset))))
#     case 3:
#         file_to_write = open('logs.txt', 'a', encoding='utf-8')

#         i = 0
#         tempVar = ''
#         while i < 33:
#             i += 1
#             print(f'Для сдвига {i}: {shift(message, i)}')
#             tempVar = tempVar + f'Для сдвига {i}: {shift(message, i)}\n'
#         file_to_write.write(tempVar)
#     case _:
#         file_to_write = open('logs.txt', 'w', encoding='utf-8')
#         print('Вы клоун')
#         file_to_write.write(
#             'ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД ГАД')

# file_to_write.close()

# # with open('logs.txt', "rb") as file:
# #     session.storbinary('filippov.txt', file)



# file_to_write.close()

# file_to_write = open('logs.txt', 'rb')


# file_to_write.close()

ALPHA_RUS = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
             'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
ALPHA_ENG = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

choice = int(input('1 - Шифрование\n2 - Дешифрование\n3 - хз\n'))
message = str(input('ТЕКСT: ')).upper()
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
        while i < 33:
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


