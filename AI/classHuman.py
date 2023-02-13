#pep8:
#Переменные: cum_peremenaya
#Фукции: cumClass
#Класс:cum_function
class Human: # Обьявление класса Human
    def say_hello(self): #Описанеи метода класса
        print("Hi, nigga!") #Self -- "Себя" -- кто исполняет(сам обьект)

    def say_this(self, message):# в методы можно передовать аргументы
        print(message)# как в обычную функцию

    def hello(self):
        self.say_this("I love this peace of shit")


nick= Human() #Создание обьекта\сущности
rick= Human()
dick= Human()

print(rick,nick,dick)

rick.say_hello()
nick.say_this("Fuck, Yourself, bitch!")
dick.hello()
