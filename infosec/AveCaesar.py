from ftplib import FTP

RUS_ALPHA = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ENG_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ftp = FTP()
HOST = 'vh388.timeweb.ru'
PORT = 21
USER = 'bormotoon_infosec'
PASSWORD = 'zfyLKkD3'

# Создаём соединение с FTP-сервером
srv = FTP()
srv.connect(HOST, PORT)
srv.login(USER, PASSWORD)





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
        file_to_write.close()  # Закрытие файла
else:
    print('Неверные данные')


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
