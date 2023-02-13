# pep8
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

print(rick, nick, dick)

rick.say_hello()
nick.say_this('Hello yourself!')
dick.hello()