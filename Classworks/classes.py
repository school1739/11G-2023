class Human:  #Создаем новый класс

  def __init__(self, name):  #Кострукотор
    print(f'Родился человек с именем {name}')  #Сообщение о создании новой сущьности
    self.__name = name  #ИНКАПСУЛИРОВАНИЕ (__) свойства
    self.__age = 0
    self.__health = 100

  @property
  def age(self):
    return self.__age

  @age.setter
  def setAge(self, newAge):
    if 1 < newAge < 100:
      self.__age = newAge


male_1 = Human('Rick')
female_1 = Human('Doro')

print(male_1.age())
male_1.setAge(28)
print(male_1.age())
male_1.setAge(150)
print(male_1.age())