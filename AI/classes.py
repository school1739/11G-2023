# Егорова и Кузнецов Г
#PEP8:
#Переменные: some_peremennaya
#Классы: SomeClass
#Функции: some_function

'''class Human: # Объявление класса
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
dick.hello()'''

#Конструктор
class Cat:
    def __init__(self, name):
        self.__name = name # свойство ИМя для обьекта класса CAT
        self.__age = 0 # __ - знак инкапсуляции


    def set_age(self, age):
        if 1<=age<=25:
            self.__age = age
        else:
            print('Мертвый')

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"My name is {self.__name}, my age is {self.__age}")

simons_cat = Cat('Rick')
print(simons_cat.get_name(), simons_cat.get_age())

'''print(simons_cat.__name, simons_cat.__age)
print(type(simons_cat.__name), type(simons_cat.__age))


simons_cat.family = 'Simpsons'
print(simons_cat.family)
simons_cat.display_info()
#the_age =
#simons_cat.age += the_age

simons_cat.set_age(25)
print(simons_cat.__cat, simons_cat.__age)'''















