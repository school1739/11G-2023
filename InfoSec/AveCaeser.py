Alphabet_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
Alphabet_EN = "ABCDEFGHIKLMNOPQRSTVXYZ"
message = input("Введите сообщение : ").upper()
offset = int(input("Введите сдвиг : "))
answer = ""
for char in message:
    if char in Alphabet_RU:
        answer += Alphabet_RU[(Alphabet_RU.find(char) + offset) % len(Alphabet_RU)]
    elif char in Alphabet_EN:
        answer += Alphabet_EN[(Alphabet_EN.find(char) + offset) % len(Alphabet_EN)]
    else:
        answer += char
print(answer)