# Переменные: some_person
# Классы: SomeClass
# Функция: some_fuction

class Human: # Объявление класса
    def say_hello(self): # Описание метода класса
        print('Hello!') # self - заставляет сущность делать самому

    def say_this(self, message): # В методы можно передавать аргументы
        print(message) # Как в обычную функцию

    def hello(self):
        self.say_this('Hello this shit!')

rick = Human() # Создание сущности/объекта класса Human
nick = Human()
dick = Human()

print(rick, nick, dick)
rick.say_hello()
nick.say_this('Hello yourself!')
dick.hello()