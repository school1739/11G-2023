#Бычков Лопатин
RUS_ALPHA = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ENG_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

offset = int(input("Введите сдвиг : "))
offset = offset % len(RUS_ALPHA)
if offset > 33: #Если полный круг
    offset = offset-33
message = input("Введите сообщение:").upper()
answer = ""

for char in message:    # отличает rus от eng
    char_place_rus = RUS_ALPHA.find(char)
    char_place_eng = ENG_ALPHA.find(char)
    new_place_rus = char_place_rus + offset
    new_place_eng = char_place_eng + offset
    if char in RUS_ALPHA:
        answer += RUS_ALPHA[new_place_rus]
    elif char in ENG_ALPHA:
        answer+=ENG_ALPHA[new_place_eng]
    else:
        answer += char
print(answer)