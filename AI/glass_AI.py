# Базанов Александр, Кузнецов Владимир
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


def player_start():  # Начало игрока
    situation = 11  # Изначальное число стаканов
    global ai_is_winner, player_wins, ai_wins, player_turn, start_ai
    while situation > 0:
        print('-' * 50)
        print(f"На столе {situation} палочек.")
        print('-' * 50)
        player_turn = True
        if situation == 1:
            print("Пользователь проиграл, осталась последняя палочка")
            ai_is_winner = True
            check_win()
        choice = int(input("Сколько палочек взять (1 или 2): "))
        while choice != 1 and choice != 2:
            choice = int(input("Сказано же, дебил, одну или две!"))  # Человек выбирает сколько взять
        situation = situation - choice  # Обновление игровой ситуации
        print('-' * 50)
        print(f"На столе {situation} палочек.")
        print('-' * 50)
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
    while situation > 0:
        player_turn = False
        print("Ход ИИ")
        situation = situation - ai_move(situation)  # Ход ИИ, обновление ситуации
        print('-' * 50)
        print(f"На столе {situation} палочек.")
        print('-' * 50)
        player_turn = True
        if situation == 1:
            print("Пользователь проиграл, осталась последняя палочка")
            ai_is_winner = True
            check_win()
        elif situation <= 0:
            if player_turn:
                ai_is_winner = False
            else:
                ai_is_winner = True
            check_win()
        choice = int(input("Сколько палочек взять (1 или 2): "))
        while choice != 1 and choice != 2:
            choice = int(input("Сказано же, дебил, одну или две!"))  # Человек выбирает сколько взять
        situation = situation - choice  # Обновление игровой ситуации
        print('-' * 50)
        print(f'На столе {situation} палочек.')
        print('-' * 50)
        player_turn = False
    if situation <= 0:
        print('-' * 50)
        print(f"На столе {situation} палочек.")
        print('-' * 50)
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
            print('=' * 70)
            print(f"Игрок:{player_wins} \nКомпьютер:{ai_wins}")
            print("Победил компьютер, он набрал 10 очков")
            print(the_glasses)
            for i in range(1, len(the_glasses) + 1):
                print('-' * 50)
                print(f'Процент выпадения 1 в {i} стаканчике:{round(the_glasses[i].count(1) / len(the_glasses[i]) * 100)} %')
                print(f'Процент выпадения 2 в {i} стаканчике:{round(the_glasses[i].count(2) / len(the_glasses[i]) * 100)} %')
            exit()
        else:
            for chosen_numbers in keys:
                the_glasses[chosen_numbers].append(used_glasses[chosen_numbers])
            print('=' * 70)
            print(f"Игрок:{player_wins} \nКомпьютер:{ai_wins}")
            print('=' * 70)
            ai_start()
    else:
        player_wins += 1
        if player_wins == 10:
            print('=' * 70)
            print(f"Игрок:{player_wins} \nКомпьютер:{ai_wins}")
            print("Победил игрок, он набрал 10 очков")
            print(the_glasses)
            for i in range(1, len(the_glasses) + 1):
                print('-' * 50)
                print(f'Процент выпадения 1 в {i} стаканчике:{round((the_glasses[i].count(1)/len(the_glasses[i]))*100)} %')
                print(f'Процент выпадения 2 в {i} стаканчике:{round(the_glasses[i].count(2) / len(the_glasses[i]) * 100)} %')
            exit()
        else:
            for chosen_numbers in keys:
                the_glasses[chosen_numbers].remove(used_glasses[chosen_numbers])
            print('=' * 70)
            print(f"Игрок:{player_wins} \nКомпьютер:{ai_wins}")
            print('=' * 70)
            player_start()


# print(the_glasses)
if player_wins == 0 and ai_wins == 0:
    player_start()
