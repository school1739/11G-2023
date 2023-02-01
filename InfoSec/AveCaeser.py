Alphabet_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
Alphabet_EN = "ABCDEFGHIKLMNOPQRSTVXYZ"
message = input("Введите сообщение : ").upper()
offset = (int(input("Введите сдвиг : ")) % len(Alphabet_RU) - 1)
answer = ""
for char in message:
    if char in Alphabet_RU:
        answer += Alphabet_RU[Alphabet_RU.find(char) + offset]
    else:
        answer += char
print(answer)