#Pep8
#Переменные: some_peremennaya
#Классы: SomeClass
#Функции: some_function


class Human:  # Объявление класса Human
    def say_hallo(self):  # Описание медота класса
        print('hello!')  # self -- 'СЕБЯ' -- кто исполняет(сам объект)


    def say_this(self, messege):  # В методы можно передовать агрументы
        print(messege)  #Как в обычную функцию


    def hello(self):
        self.say_hallo()
        self.say_this('Hello this shit!')


rick = Human()  # создание сущности(сущности) обьекта класса Human
nick = Human()
dick = Human()

print(rick, nick, dick)



dick.hello()
