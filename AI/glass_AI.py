import random  # импорт библиотеки случайных чисел
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

# Создаём словарь стаканов
the_glasses = {1: [1, 1, 1, 2, 2, 2],
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
points_ai = 0
points_user = 0
count_rounds = 1
stick = morph.parse('палочка')[0]

def move(situation):  # сделать ход (выбрать случайную бумажку из стакана и вернуть значение)
    if situation == 1:
        the_move = 1
    else:
        the_move = random.choice(the_glasses[situation])

    print('Ходит ИИ:')
    if the_move == 1:
        print(f'ИИ взял {the_move} палочку')
    else:
        print(f'ИИ взял {the_move} {stick.make_agree_with_number(the_move).word}')
    used_glasses.update({situation: the_move})
    return the_move


def used_glass_fill():  # записать использованые стаканы и бумажки
    if ai_is_winner:
        for i in used_glasses:
            the_glasses[i].append(used_glasses[i])
    else:
        for i in used_glasses:
            if used_glasses[i] in the_glasses[i]:
                the_glasses[i].remove(used_glasses[i])


while points_ai != 10 and points_user != 10:
    ai_is_winner = False
    situation = 11
    used_glasses = {}
    print('---------------------------')
    print(f'Счёт: Пользователь {points_user}:{points_ai} ИИ')
    print(f'{count_rounds}-й раунд!')
    print(f'На столе {situation} {stick.make_agree_with_number(situation).word}')
    print('---------------------------')
    while situation > 0:
        if ai_is_winner == False:
            if situation == 0:
                print("Пользователь проиграл, ИИ выиграл")
                ai_is_winner = True
            elif situation == 1:
                situation -= 1
                print('Ходит пользователь')
                print('Пользователю ничего не остаётся, кроме как взять 1 палочку')
                print(f'На столе {situation} {stick.make_agree_with_number(situation).word}')
                print("Пользователь проиграл, ИИ выиграл")
                ai_is_winner = True
                break

            choice = int(input('Сколько палочек взять? 1 или 2? '))
            while choice != 1 and choice != 2:
                choice = int(input("Сказано же, одну или две! "))  # Человек выбирает сколько взять
            situation = situation - choice  # Обновление игровой ситуации
            print(f'На столе {situation} {stick.make_agree_with_number(situation).word}')
            if situation == 0:
                print('ИИ проиграл, пользователь выиграл')
            else:
                situation = situation - move(situation)  # Ход ИИ, обновление ситуации
                print(f'На столе {situation} {stick.make_agree_with_number(situation).word}')

                if situation == 0:
                    print('ИИ проиграл, пользователь выиграл')
    count_rounds += 1

    if ai_is_winner:
        points_ai += 1
    else:
        points_user += 1

    used_glass_fill()

print(f'Окончательный счёт: Пользователь {points_user}:{points_ai} ИИ')
if points_ai > points_user:
    print('Победа ИИ')
else:
    print('Победил пользователь')






