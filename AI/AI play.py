import random
ch = 0
ai = 0
#Арзуманян Эмма Наумова Алина
the_glasses={1:[1,1,1,2,2,2],
              2:[1,1,1,2,2,2],
              3:[1,1,1,2,2,2],
              4:[1,1,1,2,2,2],
              5:[1,1,1,2,2,2],
              6:[1,1,1,2,2,2],
              7:[1,1,1,2,2,2],
              8:[1,1,1,2,2,2],
              9:[1,1,1,2,2,2],
              10:[1,1,1,2,2,2],
              11:[1,1,1,2,2,2]}

used_glasses={}
situation=11
ai_is_winner=False
def move(situation):
    print("Ходит ИИ:")
    if situation == 1:
        the_move = 1
    else:
        the_move = random.choice(the_glasses[situation])
    print(f"ИИ взял {the_move} палочек.")
    used_glasses.update({situation: the_move})
    return the_move


def used_glass_fill():
  pass
while ch < 10 and ai < 10:
    situation = 11
    print(f'Счет: {ch} : {ai}')
    print(f'На столе {situation} палочек')
    while situation > 0:
        if ai_is_winner == False:
            if situation == 0:
                print("Пользователь проиграл, ИИ выиграл")
                ai += 1
                ai_is_winner = True
            elif situation == 1:
                situation -= 1
                print('Ходит пользователь')
                print('Пользователю ничего не остаётся, кроме как взять 1 палочку')
                print(f'На столе {situation} палочек')
                print("Пользователь проиграл, ИИ выиграл")
                ai += 1
                ai_is_winner = True
                break

        choice = int(input('Сколько палочек взять? 1 или 2?'))
        while choice != 1 and choice != 2:
            choice = int(input("Сказано же, одну или две! "))
        situation = situation - choice
        print(f'На столе {situation} палочек')
        if situation == 0:
            print('ИИ проиграл, пользователь выиграл')
            ai_is_winner = False
            ch += 1
        else:
            situation = situation - move(situation)
            print(f'На столе {situation} палочек')

            if situation == 0:
                print('ИИ проиграл, пользователь выиграл')
                ai_is_winner = False
                ch += 1
if ch == 10:
    print('Пользователь победил')
    print('Конец игры')
else:
    print('ИИ победил')
    print('Конец игры')