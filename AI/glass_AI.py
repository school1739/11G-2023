import random # импорт библиотеки случайных чисел
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

used_glasses={}  # словарь использованных стаканов
ai_is_winner = True
human_wins = 0
ai_wins = 0

def move(situation): # сделать ход (выбрать случайную бумажку из стакана и вернуть значение)
  if situation == 1:
    print('Ходит ИИ:')
    the_move = 1
  else:
    if situation != 0:
      print('Ходит ИИ:')
      the_move = random.choice(the_glasses[situation])
  print(f'ИИ выбрал: {the_move}')
  used_glasses.update({situation: the_move})
  return the_move


def glass_update(used_glasses, the_glasses):
    if ai_is_winner == True:
      for key in used_glasses:
        the_glasses[key].append(used_glasses[key])
    else:
      for key in used_glasses:
        if used_glasses[key] in the_glasses[key]:
          the_glasses[key].remove(used_glasses[key])
    return the_glasses

while ai_wins != 10 and human_wins != 10:
  situation = 11
  print(f"На столе {situation} палочек.")
  while situation > 0:
    if ai_is_winner==True:
      if situation == 1:
        choice = 1
        last_choice = 'Человек'
        print('Ничего не остается, кроме как взять 1 палочку')
        situation=situation - choice
      else:
        choice=int(input('Сколько палочек взять? 1 или 2? '))
        last_choice = 'Человек'
        while choice!=1 and choice!=2:
          choice=int(input("1 или 2, необразованное чмо!!!!"))
        situation=situation - choice
        print(f"На столе {situation} палочек.")
        if situation != 0:
          situation = situation - move(situation)
          last_choice = 'ИИ'
          print(f"На столе {situation} палочек.")
    else:
      if situation != 0:
        situation = situation - move(situation)
        last_choice = 'ИИ'
        print(f"На столе {situation} палочек.")
        if situation == 1:
          choice = 1
          last_choice = 'Человек'
          print('Ничего не остается, кроме как взять 1 палочку')
          situation=situation - choice
        else:
          if situation != 0:
            choice=int(input('Сколько палочек взять? 1 или 2? '))
            last_choice = 'Человек'
            while choice!=1 and choice!=2:
              choice=int(input("1 или 2, необразованное чмо!!!!"))
            situation=situation - choice
            print(f"На столе {situation} палочек.")
  print(f'{last_choice} проиграл')
  if last_choice == 'ИИ':
    ai_is_winner = False
    human_wins += 1
  else:
    ai_is_winner = True
    ai_wins += 1
  glass_update(used_glasses, the_glasses)
  print('Счёт')
  print(f'Человек: {human_wins} ИИ: {ai_wins}')
if ai_is_winner == True:
  print('По итогам игры победил ИИ')
else:
  print('По итогам игры победил Человек')
print(the_glasses)
