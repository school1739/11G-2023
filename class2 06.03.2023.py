class Human:    # Создаем новый класс
    def __init__(self, name):  # Конструктор
        print(f"Родился человек с именем {name}!")  # Сообщение о сздании новой сущности
        self.__name = name  # ИНКАПСУЛИРОВАНИЕ (__) свойство
        self.__age = 0
        self.__health = 100
        self.__height = 35

    @property # Начало GETTER (получатель/возвращатель) - экономит место и скоряет код>>
    def age(self):     #>> делает переменую __age свойством класса Human
        return self.__age

    @age.setter # Начало SETTER ("установитель"/определитель) СВОЙСТА, задает нужное значение для >> __age
    def age(self, new_age):
        if 1<new_age<100:
            self.__age=new_age
        else:
            print('Fuck off.')

class Student(Human): #Student - подкалсс, Human-суперкласс
    def school(self):
        self.school = 1739
        print(1739)


male_1 = Human("Rick") # Создание сущности с именем Rick
female_1 = Human("Doro")
"""print(male_1.age())
male_1.set_age(15)
print(male_1.age())"""
male_1.age = 150
print(male_1.age)