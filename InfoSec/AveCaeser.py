#Гончаров Евгений
from ftplib import FTP

Host = "vh.388.timeweb.ru"
Port = 21
User = "bormotoon_infosec"
Password = "zfyLKkD3"
client = FTP()
client.connect(Host, Port)
client.login(User, Password)
client.encoding = "utf-8"

ENG_ALPHA = "ABCDEFGHIKLMNOPQRSTVXYZ"
RUS_ALPHA = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

#with open(filename, "rb") as file:
#    client.storbinary(f"STOR {filename}", file)

#with open(filename, "rb") as file:
#    client.retrbinary(f"STOR {filename}", file)
#fileToWrite = open("CaeserLog.txt", "a", encoding="utf-8")
#имя, режим работы, кодировка
#r - read
#w - write
#a - append

mode_chosen = input("Input function :\n"
                    "1 - Encrypt\n"
                    "2 - Decrypt\n"
                    "3 - Bruteforce\n"
                    "4 - Upload file\n"
                    "5 - Download file\n"
                    "6 - View the list of files\n"
                    "7 - Logout from the server\n")

while mode_chosen not in '1234567':
    mode_chosen = input("Попробуйте ввести еще раз:")
mode_chosen = int(mode_chosen)
file_to_write = open("CaesarLog.txt", "w", encoding="utf-8")
answer = ''

def encrypt():
    answer = ""
    message = input('Input a message : ').upper()
    offset = int(input('Input a offset : '))
    for char in message:
        if char in RUS_ALPHA:
            if offset > len(RUS_ALPHA):
                n = offset // len(RUS_ALPHA)
                offset = offset - n * len(RUS_ALPHA)
            rus_char_place = RUS_ALPHA.find(char)
            new_place = rus_char_place + offset 
            if new_place >= len(RUS_ALPHA):  
                new_place = new_place - len(RUS_ALPHA)
        else:
            if offset > len(ENG_ALPHA):  
                n = offset // len(ENG_ALPHA)
                offset = offset - n * len(ENG_ALPHA)
            eng_char_place = ENG_ALPHA.find(char)  
            new_place = eng_char_place + offset
            if new_place >= len(ENG_ALPHA):
                new_place = new_place - len(ENG_ALPHA)
        
        if char in RUS_ALPHA:
            answer += RUS_ALPHA[new_place]
        elif char in ENG_ALPHA:
            answer += ENG_ALPHA[new_place]
        else:
            answer += char
    file_to_write.write(f"Encrypt : {message} - {answer}")
    print(answer)

def decrypt():
    answer = ""
    message = input('Input a message : ').upper()
    offset = int(input('Input a offset : '))
    for char in message:
        if char in RUS_ALPHA[::-1]:
            if offset > len(RUS_ALPHA):
                n = offset // len(RUS_ALPHA)
                offset = offset - n * len(RUS_ALPHA)
            rus_char_place = RUS_ALPHA.find(char)
            new_place = rus_char_place - offset
            if new_place >= len(RUS_ALPHA):
                new_place = new_place - len(RUS_ALPHA)
        else:
            if offset > len(ENG_ALPHA):
                n = offset // len(ENG_ALPHA)
                offset = offset - n * len(ENG_ALPHA)
            eng_char_place = ENG_ALPHA.find(char)
            new_place = eng_char_place - offset
            if new_place >= len(ENG_ALPHA):
                new_place = new_place - len(ENG_ALPHA)
        
        if char in RUS_ALPHA:
            answer += RUS_ALPHA[new_place]
        elif char in ENG_ALPHA:
            answer += ENG_ALPHA[new_place]
        else:
            answer += char
    file_to_write.write(f"Decrypt : {message} - {answer}")
    print(answer)

def bruteforce(message, i):
    global answer
    o = "- i"
    
    for letter in message:
        if letter in ENG_ALPHA:
            answer += ENG_ALPHA[eval("(ENG_ALPHA.index(letter))" + o + "% len(ENG_ALPHA)")]
        elif letter in RUS_ALPHA:
            answer += RUS_ALPHA[eval("RUS_ALPHA.index(letter)" + o + "% len(RUS_ALPHA)")]
        else:
            answer += letter

def choose():
    global answer
    global mode_chosen
    match mode_chosen:
        case 1:
            encrypt()
        case 2:
            decrypt()
        case 3:
            message = input('Input a message : ').upper()
            file_to_write.write(message)
            for i in range(1, 32):
                bruteforce(message, i)
                file_to_write.write(f"offset {i} : {answer}, ")
                print(f"offset {i} : {answer}")
                answer = ""
        case 4:
            file_name = input("Choose the file to upload : \n")
            client.storbinary('STOR ' + file_name, open(file_name, "rb"))
        case 5:
            client.retrlines('LIST')
            file_name = input("Choose the file to download : ")
            myfile = open(file_name, 'wb')
            client.retrbinary('RETR ' + file_name, myfile.write, 1024)
            myfile.close()
        case 6:
            client.retrlines('LIST')

    mode_chosen = input("Input function :\n"
                        "1 - Encrypt\n"
                        "2 - Decrypt\n"
                        "3 - Bruteforce\n"
                        "4 - Upload file\n"
                        "5 - Download file\n"
                        "6 - View the list of files\n"
                        "7 - Logout from the server\n")

    while mode_chosen not in '1234567':
        mode_chosen = input("Incorrect input. Try again.")
    mode_chosen = int(mode_chosen)
    
while mode_chosen != 7:
    choose()
file_to_write.close()
client.quit()
