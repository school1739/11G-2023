import random

# Создаём словарь стаканов
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

used_glasses={}  # вывод словаря стаканов
situation = 11
ai_is_winner=False

def move(situation): # сделать ход (выбрать случайную бумажку из стакана и вернуть значение)
  detect = False
  print('Ходит ИИ:')
  if situation > 0:
    while detect == False:
      the_move = random.choice(the_glasses[situation])
      print(the_move)
      if situation - the_move >= 0:
        detect = True
    return the_move
  else:
    return(0)
def used_glass_fill(situation, move): # записать использованные стаканы и бумажки)
  used_glasses.update({situation:move})


#def human_move(choice):
#  return situation - choice

playerPoints = 0
botPoints = 0


while (playerPoints < 10 and botPoints < 10):
  situation = 11
  choice = 0
  player_lose = False
  print(f"На столе {situation} палочек")
  if ai_is_winner == False:
    while situation > 0:
      detect = False
      while detect == False:
        choice = int(input('Количество палочек, которое надо взять? (1 или 2)'))
        while choice!=1 and choice!=2:
          choice = int(input('Боже чел мамонт... 1 или 2 введи......... Клоун'))
        if situation - choice >= 0:
          detect = True
          print('sit: ' + str(situation))
        else:
          print('Чел клоун... Сток палок нет. Может свои принесёшь?')


      situation = situation - choice
      if situation == 0:
        player_lose = True
      print(f"На столе {situation} палочек")
      situation = situation - move(situation)
      print(f'На столе {situation} палочек')
      print()

  if (player_lose == True):
    botPoints += 1
    print('Бот затащил тебя в соло')
  else:
    playerPoints += 1
    print('Вау ты победил вау вау')

  print('Афигеть палки кончились.................')
  print(f'Счёт:\nИгрок:{playerPoints}      Бот попущенный: {botPoints}')
  print('\n\n')

print('ГЕЙМ ОВЕР ЪУЪ')
if (playerPoints == 10):
  print('Поздравляю! Победил ботика... Гордись этим всю жизнь')
elif (botPoints == 10):
  print('Чел... Тебя бот слил... Что ты делаешь в этой жизни не так?')
else:
  print(f'ТЫ СЛОМАЛ ИГРУ ИДИОТ!!! КАКИМ ОБРАЗОМ ВЫ НАБРАЛИ БОЛЬШЕ 10 ОЧКОВ!??!?!\np:{playerPoints}\nb:{botPoints}')


