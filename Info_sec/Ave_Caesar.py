RUS_ALPHA = 'АБВГДЕЁЖЗЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ENG_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

offset = int(input('Введите сдвиг: '))
offset = offset % len(RUS_ALPHA)
message = input('Введите сообщение: ').upper()
answer = ''

for char in message:
    char_place = RUS_ALPHA.find(char)
    new_place = char_place + offset
    if char in RUS_ALPHA:
        answer += RUS_ALPHA[new_place]
    elif char in ENG_ALPHA:
        answer += ENG_ALPHA[new_place]
    else:
        answer += char

print(answer)