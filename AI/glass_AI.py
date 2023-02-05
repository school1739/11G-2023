import random

# Создаём словарь со стаканами
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
               11: [1, 1, 1, 2, 2, 2]
               }
the_glasses_start_ai = {1: [1, 1, 1, 2, 2, 2],
                        2: [1, 1, 1, 2, 2, 2],
                        3: [1, 1, 1, 2, 2, 2],
                        4: [1, 1, 1, 2, 2, 2],
                        5: [1, 1, 1, 2, 2, 2],
                        6: [1, 1, 1, 2, 2, 2],
                        7: [1, 1, 1, 2, 2, 2],
                        8: [1, 1, 1, 2, 2, 2],
                        9: [1, 1, 1, 2, 2, 2],
                        10: [1, 1, 1, 2, 2, 2],
                        11: [1, 1, 1, 2, 2, 2]
                        }
used_glasses = {}  # вывод словаря стаканов
ai_is_winner = False  #
keys = used_glasses.keys()  #
player_wins = 0
ai_wins = 0
player_turn = True
start_ai = False


def ai_move(situation):  # сделать ход (выбрать случайную бумажку из стакана и вернуть значение)
    if situation == 1:
        the_move = 1
        used_glasses.update({situation: the_move})
        print(f"ИИ взял {the_move} палочку")
    else:
        the_move = random.choice(the_glasses[situation])
        used_glasses.update({situation: the_move})
        print(f"ИИ взял {the_move} палочек")
    return the_move


# def used_glass_fill(situation, move): # записать использованные стаканы и бумажки
#    used_glasses.update({situation:move})
# def human_move(choice):
#  return situation-choice
def player_start():  # Начало игрока
    situation = 11  # Изначальное число стаканов
    global ai_is_winner, player_wins, ai_wins, player_turn, start_ai
    start_ai = False
    while situation > 0:
        print(f"На столе {situation} палочек.")
        player_turn = True
        if situation == 1:
            print("Пользователь проиграл, осталась последняя палочка")
            ai_is_winner = True
            check_win()
        choice = int(input("Сколько палочек взять (1 или 2): "))
        while choice != 1 and choice != 2:
            choice = int(input("Сказано же, дебил, одну или две!"))  # Человек выбирает сколько взять
        situation = situation - choice  # Обновление игровой ситуации
        print(f"На столе {situation} палочек.")
        if situation <= 0:
            print("Пользователь проиграл")
            ai_is_winner = True
            check_win()
        print("Ход ИИ")
        player_turn = False
        situation = situation - ai_move(situation)  # Ход ИИ, обновление ситуации
        if situation <= 0:
            print("Компьютер проиграл")
            ai_is_winner = False
            check_win()


def ai_start():  # Начало компьютера
    situation = 11  # Изначальное число стаканов
    global ai_is_winner, player_wins, ai_wins, player_turn, start_ai
    start_ai = True
    while situation > 0:
        print("Ход ИИ")
        player_turn = False
        situation = situation - ai_move(situation)  # Ход ИИ, обновление ситуации
        print(f"На столе {situation} палочек.")
        player_turn = True
        if situation == 1:
            print("Пользователь проиграл, осталась последняя палочка")
            ai_is_winner = True
            check_win()
        elif situation <= 0:
            if player_turn:
                ai_is_winner = True
            else:
                ai_is_winner = False
            check_win()
        choice = int(input("Сколько палочек взять (1 или 2): "))
        while choice != 1 and choice != 2:
            choice = int(input("Сказано же, дебил, одну или две!"))  # Человек выбирает сколько взять
        situation = situation - choice  # Обновление игровой ситуации
    if situation <= 0:
        print(f"На столе {situation} палочек.")
        if player_turn:
            ai_is_winner = True
        else:
            ai_is_winner = False
        check_win()


def check_win():
    global ai_wins, player_wins
    if ai_is_winner:
        ai_wins += 1
        if ai_wins == 10:
            print(f"Игрок:{player_wins} \nКомпьютер:{ai_wins}")
            print("Победил компьютер, он набрал 10 очков")
            exit()
        if start_ai:
            for chosen_numbers in keys:
                the_glasses_start_ai[chosen_numbers].append(used_glasses[chosen_numbers])
        else:
            for chosen_numbers in keys:
                the_glasses[chosen_numbers].append(used_glasses[chosen_numbers])
        print(f"Игрок:{player_wins} \nКомпьютер:{ai_wins}")
        ai_start()
    else:
        player_wins += 1
        if player_wins == 10:
            print(f"Игрок:{player_wins} \nКомпьютер:{ai_wins}")
            print("Победил игрок, он набрал 10 очков")
            exit()
        if start_ai:
            for chosen_numbers in keys:
                the_glasses_start_ai[chosen_numbers].remove(used_glasses[chosen_numbers])
        else:
            for chosen_numbers in keys:
                the_glasses[chosen_numbers].remove(used_glasses[chosen_numbers])
        print(f"Игрок:{player_wins} \nКомпьютер:{ai_wins}")
        player_start()


# print(the_glasses)
if player_wins == 0 and ai_wins == 0:
    player_start()