RUS_ALPHA = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ENG_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

offset = int(input('Введите сдвиг: '))
message = input('Введите сообщение: ').upper()
answer = ''

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