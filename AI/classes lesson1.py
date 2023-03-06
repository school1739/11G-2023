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

print(rick, nick, dick)

rick.say_hello()
nick.say_this()