RUS_ALPHA = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ENG_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

offset = int(input('Введите сдвиг: ')) % 33
message = input('Введите сообщение: ').upper()
answer = ''

for char in message:
    char_place = RUS_ALPHA.find(char)
    new_place = char_place + offset
    if char in RUS_ALPHA:
        answer += RUS_ALPHA[new_place]
    else:
        answer += char

print(answer)