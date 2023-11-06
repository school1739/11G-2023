import random

# словарь стаканов с бумажками
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

MAX_ROUNDS = 100  # максимальное количество ходов
MAX_SCORE = 10  # максимальное количество очков

used_glasses = {}  # словарь использованных стаканов
situation = 11  # стартовая ситуация на столе
ai_is_winner = False  # маркер победы ИИ (первым ходит проигравший в прошлом раунде)

human_score = 0  # счётчик очков человека
ai_score = 0  # счётчик очков ИИ


def ai_move(situation):  # сделать ход (выбрать случайную бумажку из стакана и вернуть значение)
    print("Ходит ИИ:")
    if situation == 1:
        the_move = 1
    else:
        the_move = random.choice(the_glasses[situation])
    print(f"ИИ взял {the_move} палочек.")
    used_glasses.update({situation: the_move})
    situation -= the_move
    return the_move, situation


def human_move(situation):  # ход человека
    print("Ходит человек:")
    the_move = int(input("Введите количество палочек: "))
    the_move    return


def ai_win():
    global ai_is_winner, ai_score
    ai_is_winner = True
    ai_score += 1
    print("ИИ выиграл!")
    used_glass_fill()


def human_win():
    global ai_is_winner, human_score
    ai_is_winner = False
    human_score += 1
    print("ЧЕЛОВЕК выиграл!")
    used_glass_fill()


def used_glass_fill():  # обновляем бумажки в использованных стаканах
    if ai_is_winner:  # если ИИ победил, то в стаканы добавляются бумажки, идентичные использованным
        for key, value in used_glasses.items():
            the_glasses[key].append(value)
    else:  # если ИИ проиграл, то из стаканов убираются использованные бумажки
        for key, value in used_glasses.items():
            the_glasses[key].remove(value)

def the_round(winner):
    global situation
    while situation > 0:
        if winner == ai_is_winner:
            print("ИИ ходит первым.")
            ai_move(situation)
        else:
            print("Человек ходит первым.")
            human_move(situation)

"""def the_round():
    global situation
    while situation > 0:
        if not ai_is_winner:
            if situation == 0:
                ai_win()
            elif situation == 1:
                situation -= 1
                print('Ходит пользователь')
                print('Пользователю ничего не остаётся, кроме как взять 1 палочку')
                print(f'На столе {situation} палочек')
                ai_win()
                break
            choice = int(input('Сколько палочек взять? 1 или 2? '))
            while choice != 1 and choice != 2:
                choice = int(input("Сказано же, одну или две! "))  # Человек выбирает сколько взять
            situation = situation - choice  # Обновление игровой ситуации
            print(f'На столе {situation} палочек')
            if situation == 0:
                human_win()
            else:
                situation = situation - ai_move(situation)  # Ход ИИ, обновление ситуации
                print(f'На столе {situation} палочек')
                if situation == 0:
                    human_win()"""

print(f'На столе {situation} палочек')

while human_score < MAX_SCORE and ai_score < MAX_SCORE:
    the_round(ai_is_winner)
    situation = 11
    print(f'Счёт: {human_score} - {ai_score}')
    print(used_glasses)
    print(the_glasses)
    used_glasses.clear()
