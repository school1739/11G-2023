RUS_ALPHA = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ENG_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

offset = int(input('Введите сдвиг: '))
offset = offset % len(RUS_ALPHA)
message = input('Введите сообщение: ').upper()

answer = ''
for char in message:
    if char in RUS_ALPHA:
        char_place = RUS_ALPHA.find(char)
        new_place = char_place + offset
        if char in RUS_ALPHA:
            answer += RUS_ALPHA[new_place % len(RUS_ALPHA)]
    elif char in ENG_ALPHA:
        char_place = ENG_ALPHA.find(char)
        new_place = char_place + offset
        if char in ENG_ALPHA:
            answer += ENG_ALPHA[new_place % len(ENG_ALPHA)]
    else:
        answer += char
        

print(answer)
