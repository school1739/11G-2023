# PEP8:
# Переменные: some_var
# Классы: SomeClass
# Функции: some_function

class Human: # Объявление класса Human
    def say_hello(self): # Описание метода класса
        print('Hello!') # self -- "СЕБЯ" -- кто исполнят (сам объект)

    def say_this(self, message): # В методы можно передавать аргументы
        print(message) # Как в обычную функцию

    def hello(self):
        self.say_this('Bebra')



rick = Human() # Создание объекта (сущности) класса Human
nick = Human()
dick = Human()

dick.hello()

print(rick, nick,dick)

rick.say_hello()
nick.say_this()
dick.hello()


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


class Human:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

class Student(Human):
    def __init__(self, name):
        super().__init__(name)
        self.__grade = 0

    def study(self, univer):
        print(f'{self.name} studies in {univer}')

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade

rick = Student('rick')
rick.study('MAI')
rick.grade += 1
