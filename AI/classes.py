#PEP8:
#Переменные: some_peremennaya
#Классы: SomeClass
#Функции: some_function

class Human: # Объявление класса
    def say_hello(self): # описание метода класса
        print('Hello!') # self - 'Себя' -- кто исполняет (сам объект)

    def say_this(self, message): #В методы можно передавать аргументы
        print(message)# Как в обычную функцию

    def hello(self):
        self.say_this('Hello this shit')

rick=Human() #Создание объекта (сущности) класса Human
nick=Human()
dick=Human()

print(rick, nick, dick)

rick.say_hello()
nick.say_this('Hello yourself')
dick.hello()