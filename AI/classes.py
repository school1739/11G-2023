# Базанов Александр и Кузнецов Владимир

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
dick.hello()
