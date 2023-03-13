"""class Human:  # Создаем новый класс
    def __init__(self, name):  # Конструктор
        print(f"Родился человек с именем {name}!")  # Сообщение о создании новой сущности
        self.__name = name  # ИНКАПСУЛИРОВАННЫЕ (__) свойства
        self.__age = 0
        self.__health = 100
        self.__height = 35

    @property  # Начало GETTER (получатель/возвращатель) СВОЙСТВА
    def age(self):
        return self.__age

    @age.setter  # Начало SETTER ("установитель"/определитель) СВОЙСТВА
    def age(self, new_age):
        if 1 < new_age < 100:
            self.__age = new_age
        else:
            print("Fuck off.")


class Student(Human):
    def school(self):
        self.school = 1739
        print(1739)


male_1 = Human("Rick")  # Создание сущности класса Human с именем Rick
female_1 = Human("Doro")
"""
"""class Human:
    def __init__(self, name):
        self.name = name

    @property  # Начало GETTER (получатель/возвращатель) СВОЙСТВА
    def name(self):
        return self.__name

    @name.setter  # Начало SETTER ("установитель"/определитель) СВОЙСТВА
    def name(self, name):
        self.__name = name


class Student(Human):
    def __init__(self, name):
        super().__init__(name)
        self.__grade = 0

    def study(self, univer):
        print(f"{self.name} is in {univer}")

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade


rick = Student("Rick")
rick.study("MAI")
print(rick.grade)
rick.grade = 1
print(rick.grade)
"""


class Neuron:
    pass


class S_Neuron(Neuron):
    pass


class A_Neuron(Neuron):
    pass


class R_Neuron(Neuron):
    pass
