#сделали Егорова Женя и Мери Калантарян
import random  #берем библеотеку (рандом) она будет генерировать случайные числа для наших стаканчиков

# Далее берем и создаем сам словарь,который содержит стаканы
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

ispolzovat_stakanchiki = {}  # выводим словарь стаканов
situation = 11  # указание на изначальную позицую в игре
iskINT_is_winner = False  # флаг победы для искуственного интелекта, в новой игре ходит первый тот, кто проиграл в прошлой
def push(situation):  # функция для выполнения хода и выбора рандомной бумажки из стаканчиков
    print("Ходит Искуственный интеллект:")
    if situation == 1:
        the_push = 1
    else:
        the_push = random.choice(stakanchiki[situation])
    print(f"Иск.инт взял {the_push} палочек.")
    ispolzovat_stakanchiki.update({situation: the_push})
    return the_push

def stakanchiki_refill():
  pass
score_counter_chel = 0
score_counter_ii = 0
igrok_proigral= False
while (score_counter_chel < 10 and score_counter_ii< 10):
  situation = 11
  choice = 0
  iskINT_is_winner = False
  print(f'На столе лежат {situation} палочек')
  while situation > 0:
      if iskINT_is_winner == False:
          if situation == 0:
              print("Искуственный интелект выиграл, пользователь проиграл")
              score_counter_ii +=1
              print(f'Счет Человек   {score_counter_chel} : ИИ   {score_counter_ii}')
              iskINT_is_winner = True
          elif situation == 1:
              situation -= 1
              print('Ходит пользователь')
              print('На столе осталась 1 палочка, вам ничего не остается кроме того, как взять только 1')
              print(f'На столе лежит {situation} палочек')
              print("Пользователь проиграл, Искуственный интеллект выиграл")
              iskINT_is_winner = True
              score_counter_ii += 1
              print(f'Счет человек  {score_counter_chel} : ИИ   {score_counter_ii}')
              break

          choice = int(input('Сколько палочек берем? 1 или все таки 2?'))
          while choice != 1 and choice != 2:
              choice = int(input("нужно взять либо 1 либо 2 палочки "))  # Игроку дается выбор сколько же ему взять палочек
          situation = situation - choice  # Ситуация на столе обновляется, после хода
          print(f'На столе лежат {situation} палочек')
          if situation == 0:
              print('Искуственный интеллект проиграл, пользователь выиграл')
              score_counter_ii += 1# psjdf;qdjngqdknkfqk;knfd;lkkmng;wkmfe;kdjsnfg;skjfng;kwj  fdbk; safkbn sdf;bkejfnvbpkjhb ;vaf b;ipwtnipw
              print(f'Счет Человек  {score_counter_chel} : ИИ  {score_counter_ii}')
          else:
              situation = situation - push(situation)  # Ход Искуственного интеллекта, и снова обновляем ситуацию на столе, после хода
              print(f'На столе лежит {situation} палочек')

              if situation == 0:
                  print('Искуственный интеллект проиграл, пользователь выиграл')
                  score_counter_chel +=1
                  print(f'Счет Человек  {score_counter_chel} : ИИ  {score_counter_ii}')

  if (igrok_proigral == True):
    score_counter_ii += 1
    print('Искуственный интеллект тебя сделал')
  else:
     # он оатпждфшатвпжфыопатлфуоптхц
    print('Человек выиграл')

  print('Палочек на столе больше нет')
  print(f'Счёт:\nЧеловек:{score_counter_chel}      Искуственный интеллект: {score_counter_ii}')
  print('\n\n')

print('Игра закончилась')
if (score_counter_chel == 10):
  print('Ты выиграл комп!')
elif (score_counter_ii == 10):
  print('Тебя выиграл комп, попоробуй еще раз')
else:
  print(f'ты набрал чуть больше 10 очков, игра закончилась, но ты можешь начать снова\np:{score_counter_chel}\nb:{score_counter_ii}')
