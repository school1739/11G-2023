#Авторы: Валавин и Зинченоко
RUS_ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPORSTUVWXYZ"
ENG_ALPH = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЬЭЮЯ"

offset = int(input('Введите сдвиг:'))
message = str(input('Введите сообщение:')).upper()
answer = ''
i = 0

while (i < len(message)):
    if(message[i]in RUS_ALPH):
        newLetter = RUS_ALPH.inde (message[i]) + offset
        if newLetter >= 33:
            newLetter = newLetter - 33
        answer = answer + RUS_ALPH[newLetter]
    elif (message[i] in ENG_ALPH):
        if(message[i] in ENG_ALPH):
            newLetter = ENG_ALPH.index(message[i]) + offset
            if newLetter >= 26:
                newLetter = newLetter - 26
            answer = answer + ENG_ALPH[newLetter]
    else:
        answer = answer + message[i]
    i = i + 1
print(answer)
