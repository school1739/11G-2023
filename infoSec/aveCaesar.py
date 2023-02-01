# Филиппов и Савченко (10Ж)

ALPHA_RUS = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
             'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
ALPHA_ENG = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

offset = int(input())
message = str(input()).upper()
answer = ''
i = 0

while (i < len(message)):
    if (message[i] in ALPHA_RUS):
        newLetter = ALPHA_RUS.index(message[i]) + offset
        if newLetter >= 33:
            newLetter = newLetter - 33
        answer = answer + ALPHA_RUS[newLetter]
    elif (message[i] in ALPHA_ENG):
        if (message[i] in ALPHA_ENG):
            newLetter = ALPHA_ENG.index(message[i]) + offset
            if newLetter >= 26:
                newLetter = newLetter - 26
            answer = answer + ALPHA_ENG[newLetter]
    else:
        answer = answer + message[i]
    i = i + 1

print(answer)
