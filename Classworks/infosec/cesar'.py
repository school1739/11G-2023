RUS_ALPHA='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ENG_ALPHA='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

offset=int(input('Введите сдвиг: '))
if offset>33: #1 если полный круг
    offset=offset-33
message =(input('Введите сообщение: ')).upper()
answer=''
for char in message:
    char_place_rus=RUS_ALPHA.find(char)
    char_place_eng = ENG_ALPHA.find(char) #3 отличает рус от англ
    new_place_rus =char_place_rus+(offset%33)# если элемент в конце алф
    new_place_eng = char_place_eng + (offset%26)
    if char in RUS_ALPHA:
        answer+=RUS_ALPHA[new_place_rus%33]
    elif char in ENG_ALPHA:
        answer+=ENG_ALPHA[new_place_eng%26]
    else :
        answer +=char
print(answer)