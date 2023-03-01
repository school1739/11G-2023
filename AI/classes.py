"""# PEP8:
# Переменные: some_peremennaya
# Классы: SomeClass
# Функции: some_function

class Human:  # Объявление класса Human
    def say_hello(self):  # Описание метода класса
        print("Hello!")  # self -- "СЕБЯ" -- кто исполняет (сам объект)

    def say_this(self, message):  # В методы можно передавать аргументы
        print(message)  # Как в обычную функцию

    def hello(self):
        self.say_this("Hello this shit!")
        self.say_this("Hello again")
        self.say_this("Hello 3")


rick = Human()  # Создание объекта (сущности) класса Human
nick = Human()
dick = Human()

print(rick, nick, dick)

rick.say_hello()
nick.say_this("Hello yourself!")
dick.hello()

"""


# The Classes. Lesson 2.

# Конструктор
class Cat:
    def __init__(self, name):
        self.__name = name  # Свойство ИМЯ для объекта класса Cat
        self.__age = 0  # __ - знак инкапсуляции

    def set_age(self, age):
        if 1 <= age <= 25:
            self.__age = age
        else:
            print("Ты лошара (С) Roni")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"My name is {self.__name}, my age is {self.__age}.")


"""simons_cat = Cat("Rick")
print(simons_cat)
print(simons_cat.__name, simons_cat.age)
print(type(simons_cat.name), type(simons_cat.age))

simons_cat.family = "Simpsons"
print(simons_cat.family)

simons_cat.display_info()

simons_cat.set_age(25)
simons_cat.age += 10
print(simons_cat.name, simons_cat.age)
"""

simons_cat = Cat("Nick")
print(simons_cat.get_name(), simons_cat.get_age())
simons_cat.display_info()

simons_cat.name="Dick"
print(simons_cat.get_name())