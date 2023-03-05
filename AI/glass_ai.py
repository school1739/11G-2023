# АВТОР: Гончаров Евгений
import random # импорт библиотеки случайных чисел

# Создаём словарь стаканов
the_glasses={1:[1,1,1,1,1,2,2,2,2,2],
             2:[1,1,1,1,1,2,2,2,2,2],
             3:[1,1,1,1,1,2,2,2,2,2],
             4:[1,1,1,1,1,2,2,2,2,2],
             5:[1,1,1,1,1,2,2,2,2,2],
             6:[1,1,1,1,1,2,2,2,2,2],
             7:[1,1,1,1,1,2,2,2,2,2],
             8:[1,1,1,1,1,2,2,2,2,2],
             9:[1,1,1,1,1,2,2,2,2,2],
             10:[1,1,1,1,1,2,2,2,2,2],
             11:[1,1,1,1,1,2,2,2,2,2]}
used_glasses={}  # вывод словаря стаканов

def aiTurn(situation):
  print("Ходит ИИ:")
  move = 0
  if situation == 1:
    move = 1
  else:
    if len(the_glasses[situation]) == 0:
      move = random.choice([1, 2])
    else:
      move = random.choice(the_glasses[situation])
  print(f"ИИ выбрал : {move}")
  used_glasses.update({situation: move})
  return move

def humanTurn(situation):
  print("Ходит Человек:")
  move = 0
  if situation == 1:
    move = 1
  else:
    move = input("Выберите число 1 или 2 : ")
    while int(move) != 1 and int(move) != 2:
      move = input("Некорректный ввод. Выберите число 1 или 2 : ")
  print(f"Человек выбрал : {int(move)}")
  return int(move)

def glassUpdate(aiLastWin):
    if aiLastWin == True:
      for key in used_glasses:
        the_glasses[key].append(used_glasses[key])
    else:
      for key in used_glasses:
        if used_glasses[key] in the_glasses[key]:
          the_glasses[key].remove(used_glasses[key])
    return the_glasses

def listCount(_list, element):
    count = 0
    for e in _list:
      if e == element:
        count += 1
    return count

def main(wins):
  aiWins = 0
  humanWins = 0
  aiLastWin = False
  used_glasses = {}
  while aiWins < wins and humanWins < wins:
    situation = 11
    if aiLastWin == True:
      print("-----------------------------")
      print(f"На столе {situation} палочек.")
      situation -= humanTurn(situation)
    while situation >= 0:
      if situation == 0:
        print("человек проиграл")
        aiLastWin = True
        glassUpdate(aiLastWin)
        aiWins += 1
        break
      else:
        situation -= aiTurn(situation)
      print("-----------------------------")
      print(f"На столе {situation} палочек.")
      if situation == 0:
        print("AI проиграл")
        aiLastWin = False
        glassUpdate(aiLastWin)
        humanWins += 1
        break
      else:
        situation -= humanTurn(situation)
      print("-----------------------------")
      print(f"На столе {situation} палочек.")
    print("-----------------------------")
    print(the_glasses)
    print("-----------------------------")
  if humanWins > aiWins:
    print("Человек победил")
  else:
    print("AI победил")
  print("-----------------------------")
  print("Вероятность")
  for i in range(1,len(the_glasses)+1):
      print(f"Стакан {i}: 1:{listCount(the_glasses[i], 1)/len(the_glasses[i])} 2:{listCount(the_glasses[i], 2)/len(the_glasses[i])}")

main(10)
