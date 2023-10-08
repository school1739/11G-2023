import random


stakanchiki = {1: [1, 1, 1, 2, 2, 2],
               2: [1, 1, 1, 2, 2, 2],
               3: [1, 1, 1, 2, 2, 2],
               4: [1, 1, 1, 2, 2, 2],
               5: [1, 1, 1, 2, 2, 2],
               6: [1, 1, 1, 2, 2, 2],
               7: [1, 1, 1, 2, 2, 2],
               8: [1, 1, 1, 2, 2, 2],
               9: [1, 1, 1, 2, 2, 2],
               10: [1, 1, 1, 2, 2, 2],
               11: [1, 1, 1, 2, 2, 2]}
Ick_int_points = 0
pols_points = 0
count_rounds = 1

def move(situation):
    if situation == 1:
        the_move = 1
    else:
        the_move = random.choice(stakanchiki[situation])

    print('Ходит ИИ:')
    if the_move == 1:
        print(f'ИИ взял 1 палочку')
    else:
        print(f'ИИ взял {the_move} палочек')
    used_glasses.update({situation: the_move})
    return the_move


def used_glass_fill():
    if Ick_int_winner:
        for i in used_glasses:
            stakanchiki[i].append(used_glasses[i])
    else:
        for i in used_glasses:
            if used_glasses[i] in stakanchiki[i]:
                stakanchiki[i].remove(used_glasses[i])


while Ick_int_points != 10 and pols_points != 10:
    Ick_int_winner = False
    situation = 11
    used_glasses = {}
    print('---------------------------')
    print(f'Счёт: Пользователь {pols_points}:{Ick_int_points} ИИ')
    print(f'{count_rounds}-й раунд!')
    print(f'На столе {situation} палочек')
    print('---------------------------')
    while situation > 0:
        if Ick_int_winner == False:
            if situation == 0:
                print("Пользователь проиграл, ИИ выиграл")
                Ick_int_winner = True
            elif situation == 1:
                situation -= 1
                print('Ходит пользователь')
                print('Пользователю ничего не остаётся, кроме как взять 1 палочку')
                print(f'На столе {situation} палочек')
                print("Пользователь проиграл, ИИ выиграл")
                Ick_int_winner = True
                break

            choice = int(input('Сколько палочек взять? 1 или 2? '))
            while choice != 1 and choice != 2:
                choice = int(input("Сказано же, одну или две! "))
            situation = situation - choice
            print(f'На столе {situation} палочек')
            if situation == 0:
                print('ИИ проиграл, пользователь выиграл')
            else:
                situation = situation - move(situation)
                print(f'На столе {situation} палочек')

                if situation == 0:
                    print('ИИ проиграл, пользователь выиграл')
    count_rounds += 1

    if Ick_int_winner:
        Ick_int_points += 1
    else:
        pols_points += 1

    used_glass_fill()

print()
print('---------------------------')
print(f'Окончательный счёт: Пользователь {pols_points}:{Ick_int_points} ИИ')
if Ick_int_points > pols_points:
    print('Победа ИИ')
else:
    print('Победил пользователь')
print('---------------------------')
print()
print('Вывод содержимого стаканов')
for number, content in stakanchiki.items():
    print(f'{number}-й стакан: {content}')
print('---------------------------')
print()
print('Вывод шанса выпадения 1 или 2 для каждого стакана')
for number, content in stakanchiki.items():
    try:
        print(f'{number}-й стакан:\nШанс выпадения 1 - {round((content.count(1)/len(content))*100, 1)}%\nШанс выпадения 2 - {round((content.count(2)/len(content))*100, 1)}%')
    except:
        print(f'{number}-й стакан:\nШанс выпадения 1 - 0.0%\nШанс выпадения 2 - 0.0%')

