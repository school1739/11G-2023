class Human: # Создаем новый класс
    def __init__(self, name): # Конструктор
        print(f'Родился человек с именем {name}!') # Сообщение о создании сущности
        self.__name=name # Инкапсулирование(__) свойства
        self.__age=0
        self.__health=100

    @property # Начало GETTER (получатель/возвращатель)
    def age(self):
        return self.__age
    @age.setter # Начало SETTER (установитель/определитель) Свойства
    def age(self, new_age):
        if 1<new_age<100:
            self.__age=new_age
        else:
            print('Fuck off.')

class Student(Human): # подкласс студент
    def school(self):
        self.school=1739
        print(1739)


male_1=Human('Rick')
female_1=Human('Doro')
'''print(male_1.age())
male_1.set_age(15)
print(male_1.age())'''
print(male_1.age)

male_1.age=15
print(male_1.age)

