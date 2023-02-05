# авторы: Миронова София, Хохлова Наталия

import random # импорт библиотеки рандомных чисел
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
win_glasses = {} # вывод словаря стаканов
situation = 11 # начальная позиция в игре
ai_is_winner = False # флаг победы для ии, в новой игре ходит первый тот, кто проиграл в прошлой

def move(situation): # сделать ход(выбрать случайную бумажку из стакана и вернуть значение)
  print('Ход ИИ')
  if situation == 1:
    the_move = 1
  else:
    the_move = random.choice(the_glasses[situation])
  print(f'ИИ выбрал {the_move} палочек')
  win_glasses.update({situation: the_move})
  return the_move

def win_glasses_fill():
  pass


score_player = 0
score_ii = 0
player_lost = False
while (score_player < 10 and score_ii < 10):
    situation = 11
    choice = 0
    ai_is_winner = False
    print(f'На столе {situation} палочек')
    while situation > 0:
        if ai_is_winner == False:
            if situation == 0:
                print("Игрок проиграл, ИИ выиграл")
                score_ii += 1
                print(f'Счет Игрок:{score_player}   ИИ:{score_ii}')
                ai_is_winner = True
            elif situation == 1:
                situation -= 1
                print('Ходит игрок')
                print('Игроку ничего не остаётся, кроме как взять 1 палочку')
                print(f'На столе {situation} палочек')
                print("Игрок проиграл, ИИ выиграл")
                ai_is_winner = True
                score_ii += 1
                print(f'Счет Игрок:{score_player}   ИИ:{score_ii}')
                break

            choice = int(input('Сколько палочек взять? 1 или 2?'))
            while choice != 1 and choice != 2:
                choice = int(input("Сказано же, одну или две! "))  # игрок выбирает сколько палочек взять
            situation = situation - choice  # обновление игровой ситуации
            print(f'На столе {situation} палочек')
            if situation == 0:
                print('ИИ проиграл, игрок выиграл')
                score_ii += 1
                print(f'Счет Игрок:{score_player}   ИИ:{score_ii}')
            else:
                situation = situation - move(situation)  # ход ИИ, обновление ситуации
                print(f'На столе {situation} палочек')
                if situation == 0:
                    print('ИИ проиграл, игрок выиграл')
                    score_player += 1
                    print(f'Счет Игрок:{score_player}   ИИ:{score_ii}')

    if (player_lost == True):
        score_ii += 1
        print('ИИ победил')
    else:
        print('Игрок победил')

    print('Палочек на столе не осталось')
    print(f'Счет: \nИгрок: {score_player}   ИИ: {score_ii}')
    print()

print('Игра окончена')
if (score_player == 10):
    print('Победа игрока!')
elif (score_ii == 10):
    print('Победа ИИ!')
else:
    print(f'Игрок набрал больше 10 очков, можно начать заново')