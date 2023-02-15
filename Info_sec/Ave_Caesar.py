# Базанов, Кузнецов В., Егорова
RUS_ALPHA = 'АБВГДЕЁЖЗЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ENG_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
int(input("Введите функцию:\n1 - Шифрование\n2 - Дешифровка\n3 - Bruteforce"))


def encrypt():
    offset = int(input('Введите сдвиг: '))
    # offset = offset % len(RUS_ALPHA)
    message = input('Введите сообщение: ').upper()
    answer = ''
    if offset > len(RUS_ALPHA):
        n = offset // len(RUS_ALPHA)
        offset = offset - n * len(RUS_ALPHA)
    elif offset > len(ENG_ALPHA):
        n = offset // len(ENG_ALPHA)
        offset = offset - n * len(ENG_ALPHA)
    for char in message:
        if message in RUS_ALPHA:
            rus_char_place = RUS_ALPHA.find(char)
            new_place = rus_char_place + offset
        else:
            eng_char_place = ENG_ALPHA.find(char)
            new_place = eng_char_place + offset
        if new_place > len(RUS_ALPHA):
            new_place = new_place - len(RUS_ALPHA)
        elif new_place > len(ENG_ALPHA):
            new_place = new_place - len(ENG_ALPHA)
        if char in RUS_ALPHA:
            answer += RUS_ALPHA[new_place]
        elif char in ENG_ALPHA:
            answer += ENG_ALPHA[new_place]
        else:
            answer += char
        print(answer)

