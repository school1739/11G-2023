RUS_ALPHA = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ENG_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

made_choice = int(input('Выберите операцию:'
                        ' 1 - шифрование'
                        ' 2 - дешифровка'
                        ' 3 - перебор'))

message = input('Введите сообщение: ').upper()
answer = ''
nomer = 0
if made_choice == 1:
    offset = int(input('Введите сдвиг: '))
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

if made_choice == 2:
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

if made_choice == 3:
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
        print(nomer, answer)

