#АвфтоРррррряр:Валавин Дунил




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
          choice = int(input('Ты додик или да? Сказано же 1 или 2'))
        if situation - choice >= 0:
          detect = True
          print('sit: ' + str(situation))
        else:
          print('Я конечно знал то ты умственно отсталый, но брать палки из воздуха я неумею сорри')


      situation = situation - choice
      if situation == 0:
        player_lose = True
      print(f"На столе {situation} палочек")
      situation = situation - move(situation)
      print(f'На столе {situation} палочек')
      print()

  if (player_lose == True):
    botPoints += 1
    print('ИИ ТЕБЯ ЖОЙСКО ПОПУСТИЛ, БОТИК')
  else:
    playerPoints += 1
    print('Нифига, ты победил, нигга')

  print('Блин паклки кончались(. Я в магаз за новыми')
  print(f'Счёт:\nИгрок:{playerPoints}          Чмошный ИИ: {botPoints}')
  print('\n\n')

print('ГАМЕ ОВЭР ЛОЛ')
if (playerPoints == 10):
  print('Поздравляю!ТЫ ЖОЙСКО попустил бота,можешь похвастаться своей пятке')
elif (botPoints == 10):
  print('АПХПХПХПХ НУ ТЫ ЛОХ АПХПХПХХАХП БОТИКУ ПРОИГРАЛ XD')
else:
  print(f'У меня вопрос: КАК ТЫ СЛОМАЛ ИГРУ, АМОГУС?!?!??!\np:{playerPoints}\nb:{botPoints}')


