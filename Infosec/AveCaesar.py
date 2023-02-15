RUS_ALPHA = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ENG_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

file_to_write = open("CaesarBebra.txt", "w", encoding='utf-8')
mode = int(input('Введите режим: '))
while str(mode) not in '123':
    mode = int(input())
message = input('Введите сообщение: ').upper()
offset = int(input('Введите сдвиг: '))
def encrypt(offset, message):
    offset = int(offset)
    offset = offset % len(RUS_ALPHA)
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
    print(f'Сдвиг {offset}: {answer}')
    file_to_write.write(answer)

def decrypt(offset, message):
    offset = int(offset)
    offset = offset % len(RUS_ALPHA)

    answer = ''
    for char in message:
        if char in RUS_ALPHA:
            char_place = RUS_ALPHA.find(char)
            new_place = char_place - offset
            if char in RUS_ALPHA:
                answer += RUS_ALPHA[new_place % len(RUS_ALPHA)]
        elif char in ENG_ALPHA:
            char_place = ENG_ALPHA.find(char)
            new_place = char_place - offset
            if char in ENG_ALPHA:
                answer += ENG_ALPHA[new_place % len(ENG_ALPHA)]
        else:
            answer += char
    print(answer)
    file_to_write.write(answer)

def bruteforce(message):
    for i in range(1, 32):
        encrypt(i, message)


match mode:
     case 1:
         encrypt(offset, message)
     case 2:
         decrypt(offset, message)
     case 3:
         bruteforce(message)
     case _:
         print("Нет такого режима")
