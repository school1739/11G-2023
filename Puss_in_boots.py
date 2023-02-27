# Конструктор
class Cat:
  def __init__(self, name):
    self.__name = name # Свойство ИМЯ для объекта класса Cat
    self.__age = 0 # __ - знак инкапсуляции
    
  def set_age(self, age):
    if (1 <= age < 25):
      self.__age = age
    else: print('Ты лоШАРА (c) Я')
  def displayInfo(self):
    print(f"My name is {self.__name}, my age is {self.__age}")
  def get_age(self):
    return self.__age
  def get_name(self):
    return self.__name






    
simons_cat = Cat("Puss_in_boots")
# print(simons_cat)
# print(simons_cat.name, simons_cat.age)
# print(type(simons_cat.name), type(simons_cat.age))

# simons_cat.family = 'Simpsons'
# print(simons_cat.family)

# simons_cat.displayInfo()
# simons_cat.age += 5
# print(simons_cat.age)

# deAge = int(input("Введите возраст новый возраст кота: "))
simons_cat.set_age(21)
# simons_cat.age += 10

simons_cat.displayInfo()
print(simons_cat.get_age(), simons_cat.get_name())
