'''# Базанов Александр и Кузнецов Владимир

# PEP8:
# Переменные: some_peremen
# Классы: Someclass
# Функции: some_function

class Human:
    def say_hello(self):  # Описание метода класса
        print('Hello')  # self -- "СЕБЯ" -- кто исполняет (сам объект)

    def say_this(self, message):  # В методы можно передавать аргументы
        print(message)  # Как в обычной функции

    def hello(self):
        self.say_this('Hello this shit!')


rick = Human()  # Создание объекта (сущности) класса Human
nick = Human()
dick = Human()

print(rick, nick, dick)

rick.say_hello()
nick.say_this('Hello yourself!')
dick.hello()'''


# The Classes. Lesson 2


# Конструктор
class Cat:
    def __init__(self, name):
        self.__name = name  # Свойство ИМЯ для объекта класса Cat
        self.__age = 0 # __ - знак икапсуляции

    def set_age(self, age):
        if 1 <= age <= 25:
            self.age = age
        else:
            print("Ты лошара (С) Roni")

    def display_info(self):
        print(f"My name is {self.name}, my age is {self.age}.")


simons_cat = Cat("Rick")
print(simons_cat.name, simons_cat.age)
print(type(simons_cat.name), type(simons_cat.age))

simons_cat.family = "Simpsons"
print(simons_cat.family)
simons_cat.display_info()

simons_cat.set_age(30)
print(simons_cat.name, simons_cat.age)
