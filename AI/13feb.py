# PEP8:
# Переменные и функции: some_variable; someVariable
# Классы: SomeClass


class Human: # Объявление класса Human
    def say_hello(self): # Метод класса say_hello; [self] - "СЕБЯ"; кто исполняет
        print("Hello!1")

    def say_smth(self, msg): # В методы можно передавать аргументы как в обычную функцию
        print(msg)

    def hello(self):
        self.say_smth('ПУК ПУК ПУУУК)))') # При помощи self можно обращаться к другим методам этого класса
rick = Human() # Создание объекта (entity) класса Human
nick = Human()
dick = Human()

print(rick, nick, dick)

rick.say_hello()
nick.say_smth('БЛЭК ВОТЫРР!1')
dick.hello()