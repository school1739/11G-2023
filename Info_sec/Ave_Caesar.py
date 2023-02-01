# Базанов, Кузнецов В., Егорова
RUS_ALPHA = 'АБВГДЕЁЖЗЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ENG_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

offset = int(input('Введите сдвиг: '))
# offset = offset % len(RUS_ALPHA)
message = input('Введите сообщение: ').upper()
answer = ''
if offset > len(RUS_ALPHA):
    n = offset // len(RUS_ALPHA)
    offset = offset - n * len(RUS_ALPHA)
for char in message:
    char_place = RUS_ALPHA.find(char)
    new_place = char_place + offset
    if new_place > len(RUS_ALPHA):
        new_place = new_place - len(RUS_ALPHA)
    if char in RUS_ALPHA:
        answer += RUS_ALPHA[new_place]
    elif char in ENG_ALPHA:
        answer += ENG_ALPHA[new_place]
    else:
        answer += char

print(answer)
