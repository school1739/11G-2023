#Филиппов, Зинченко
#x = int(input('Введите длину таблицы: '))
matrix = [[2, 4, 1,1],
         [0, 2, 0, 0],
         [2, 1, 1, 3],
         [4, 0, 2, 3]]


def minor(input, i, j):
  output = []
  for counter in range(0, len(input)):
    output.append(input[counter])
    temp = output[counter].pop(j)

  temp = output.pop(i)

  for counter in range(len(output)):
    output[counter].append(output[counter][0])
    output[counter].append(output[counter][1])


  for counter in range(3):

  print(output)
  return output
  # for counter in range(0, len(output)):
  #   summ = summ + sum(output[counter])

  # return(summ)

  

print(minor(matrix, 1, 1))

# Метод	Что делает
# list.append(x)	Добавляет элемент в конец списка
# list.extend(L)	Расширяет список list, добавляя в конец все элементы списка L
# list.insert(i, x)	Вставляет на i-ый элемент значение x
# list.remove(x)	Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
# list.pop([i])	Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
# list.index(x, [start [, end]])	Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
# list.count(x)	Возвращает количество элементов со значением x
# list.sort([key=функция])	Сортирует список на основе функции
# list.reverse()	Разворачивает список
# list.copy()	Поверхностная копия списка
# list.clear()	Очищает список