mode_choice = int(input("Выберите режим работы: 1 - шифрование, 2 - дешифрование, 3 - bruteforce: "))
RUS_ALPHA = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ENG_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

text = input("Введите текст: ").upper()
answer = ""


def iterate_text(text, mode):
    global answer
    match mode:
        case "encrypt":
            op = "+ offset"
        case "decrypt":
            op = "- offset"
        case "bruteforce":
            op = "- i"
    for letter in text:
        if letter in RUS_ALPHA:
            answer += RUS_ALPHA[eval("RUS_ALPHA.index(letter)" + op + "% len(RUS_ALPHA)")]
        elif letter in ENG_ALPHA:
            answer += ENG_ALPHA[eval("(ENG_ALPHA.index(letter)" + op + "% len(ENG_ALPHA)")]
        else:
            answer += letter


match mode_choice:
    case 1:
        offset = int(input("Введите сдвиг: "))
        iterate_text(text, "encrypt")
        print(answer)

    case 2:
        offset = int(input("Введите сдвиг: "))
        iterate_text(text, "decrypt")
        print(answer)

    case 3:
        for i in range(1, 32):
            iterate_text(text, "bruteforce")
            print(f"Сдвиг {i}: {answer}")
            answer = ""

    case _:
        print("Неверный режим работы")
