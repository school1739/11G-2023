from ftplib import FTP

RUS_ALPHA = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ENG_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ftp = FTP()
HOST = 'vh388.timeweb.ru'
PORT = 21
USER = 'bormotoon_infosec'
PASSWORD = 'zfyLKkD3'

ftp.connect(HOST, PORT)
ftp.login(USER, PASSWORD)





#file_to_write = open("Caesar(salad).txt", "w", encoding="utf-8") # Открытие файла для записи ответов
# аргументы : имя файла, режим работы, кодировка
# режим работы:
        # "r" - read(только чтение)
        # "w" - write(запись)
        # "a" - append(добавить в конец)

made_choice = int(input('Выберите операцию:\n'
                    ' 1 - шифрование\n'
                    ' 2 - дешифровка\n'
                    ' 3 - bruteforce\n'))

message = input('Введите сообщение: ').upper()
answer = ''
nomer = 0

if made_choice == 1:
    offset = int(input('Введите сдвиг: '))
    file_to_write = open("Caesar(salad).txt", "w", encoding="utf-8")
    for char in message:
        if char in RUS_ALPHA:
            char_place = RUS_ALPHA.find(char)
            new_place = char_place + (offset % 33)
            answer += RUS_ALPHA[new_place % 33]
        elif char in ENG_ALPHA:
            char_place = ENG_ALPHA.find(char)
            new_place = char_place + (offset % 26)
            answer += ENG_ALPHA[new_place % 26]
        else:
            answer += char
    print(answer)
    file_to_write.write(f'{answer} \n') # Запись в файл
elif made_choice == 2:
    file_to_write = open("Caesar(salad).txt", "w", encoding="utf-8")
    offset = int(input('Введите сдвиг: '))
    for char in message:
        if char in RUS_ALPHA:
            char_place = RUS_ALPHA.find(char)
            new_place = char_place - (offset % 33)
            answer += RUS_ALPHA[new_place % 33]
        elif char in ENG_ALPHA:
            char_place = ENG_ALPHA.find(char)
            new_place = char_place - (offset % 26)
            answer += ENG_ALPHA[new_place % 26]
        else:
            answer += char
    print(answer)
    file_to_write.write(f'{answer} \n')   # Запись в файл
elif made_choice == 3:
    file_to_write = open("Caesar(salad).txt", "a", encoding="utf-8")
    for offset in range(32):
        answer = ''
        nomer += 1
        for char in message:
            if char in RUS_ALPHA:
                char_place = RUS_ALPHA.find(char)
                new_place = char_place - (offset % 33)
                answer += RUS_ALPHA[new_place % 33]
            elif char in ENG_ALPHA:
                char_place = ENG_ALPHA.find(char)
                new_place = char_place - (offset % 26)
                answer += ENG_ALPHA[new_place % 26]
            else:
                answer += char
        print(answer)
        file_to_write.write(f'{nomer}. {answer} \n') # Запись в файл
else:
    print('Неверные данные')
file_to_write.close()