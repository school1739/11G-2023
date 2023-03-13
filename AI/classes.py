'''# pep8
# Переменные some_peremennaya
# Классы: SomeClass
# Функции: some_function

class Human:  # Объявление класса Human
    def say_hello(self):   # описание метода классов
        print("Hello!")    # self -- "СЕБЯ" -- кто исполняет (сам объект)

    def say_this(self, message):          # В методы можно ззаписывать аргументы
        print(message)    # как в обычную функцию

    def hello(self):
        self.say_this('Hello this shit!')

rick = Human()   # Создание объекта (сущности) класса Human
nick = Human()
dick = Human()

print(rick, nick, dick) #123

rick.say_hello()
nick.say_this('Hello yourself!')
dick.hello()


# Lesson 2

# Конструктор
class Cat:
    def __init__(self, name):
        self.__name=name # Свойство ИМЯ для объекта класса Cate
        self.__age = 0  # __ - знак инкапсуляции
    def set_age(self, age):
        if 1<=age<=25:
            self.age=age
        else:
            print('у тебя нет кота (C) Roni')
    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print(f'My name is {self.__name}, my age is {self.__age}.')



'''

'''simons_cat =Cat('Rick')
print(simons_cat)
print(simons_cat.name, simons_cat.age)
print(type(simons_cat.name), type(simons_cat.age))

simons_cat.family = 'Simpsons'
print(simons_cat.family)

simons_cat.display_info()

the_age=int(input('Введите новый возраст кота'))
simons_cat.age += the_age

simons_cat.set_age(25)
print(simons_cat.__age, simons_cat.__name)


simons_cat = Cat('Nick')
print(simons_cat.get_name(), simons_cat.get_age())

simons_cat.name='Dick'
print(simons_cat.get_name())
 # 123
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

'''
class Human():
    def __init__(self, _name):
        print(f"Родился человек с именем {_name}")
        self.name = _name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_name):
        self.name = new_name

class Student(Human):
    def __init__(self, _name):
        super().__init__(_name)
        self.grade = None
        self.univer = None

    def study(self, _univer):
        print(f"{self.name} is in {_univer}")
        self.univer = _univer

    @property
    def grade(self):
        print()
        return self.grade

    @grade.setter
    def grade(self, _grade):
        self.grade = _grade

rick = Student("rick")
rick.study("МАИ")
rick.study(1)
print(rick.univer)'''