# PEP8:
# Переменные: some_peremen
# Классы: Someclass
# Функции: some_function

'''
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


'''




class Human:
    def __init__(self):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name_set(self, name):
        self.__name = name


class Student(Human):
    def __init__(self, name):
        self.__name = name

    def study(self, univer):
        print(f"{self.name} is in {univer}")

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(selfself, grade):
        self.__grade = grade


rick = student("Rick")
rick.study("MAI")
print(rick.grade)
rick.grade = 1
print(rick.grade)

rick = Human('Rick')
print(rick.name)