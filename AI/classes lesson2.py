# Лишанков Шарапов
class Human: # Создаем новый класс
    def __init__(self, name): # Конструктор
        print(f'Родился человек с именем {name}!') # Сообщение о создании новой сущности
        self.__name = name # инкапсулированные свойства
        self.__age = 0
        self.__health = 100
        self.__height = 35

    @property # Начало Getter (получатель/возвращатель)
    def age(self):
        return self.__age

    @age.setter # Начало Setter (установитель) свойства
    def age(self, new_age):
        if 1<new_age<100:
            self.__age = new_age
        else:
            print('No.')

class Student(Human):
    def school(self):
        self.school = 1739
        print()


male_1 = Human('Rick') # Создание сущности класса Human с именем Rick
female_1 = Human('Doro')

