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
'''class Cat:
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
print(simons_cat.get_name(), simons_cat.get_age())'''

'''print(simons_cat.__name, simons_cat.__age)
print(type(simons_cat.__name), type(simons_cat.__age))


simons_cat.family = 'Simpsons'
print(simons_cat.family)
simons_cat.display_info()
#the_age =
#simons_cat.age += the_age

simons_cat.set_age(25)
print(simons_cat.__cat, simons_cat.__age)'''



class Human: # Объявление класса
    def __init__(self, name): # описание метода класса, __innit__ встроенный конструктор ( self, name- можем принять name(аргумент))
        self.__name = name # создаем инкапсулированную переменную(заприваченную), которой присваеваем значение из полученного аргумента

    @property # штука, говорящая, что name - НЕ просто переменная, которая что-то содержит!
    #property - свойство HUMAN, записанное в переменной name
    def name(self):
        return self.__name = name          # свойство записанное в переменной name


    @name.setter # Для возможности изменения свойства name, чтобы можно было менять инкапсулированную переменную только когда мы напишем Human.name =.......)
    def name(self, name):# можно для любой сущности которая содержит этот класс
        self.__name = name  # что бы ничего не менялось до того пока не скажем



class Student(Human):# подкласс для Human
    def __init__(self, family_name): # обращается именно к конструктору
        super().__init__(family_name) # super - к какому супер классу, название функции/ метода
        # название аргумента не влияет на содержание, то что было в family_name перейдет в name
        self.__grade = 0

    @property
    def grade(self):#свойство у студента - grade, у Human такого нет
        return self.__grade
    @grade.setter # что бы можно было изменять grade, но сам он накручивать не сможет, пока мы не запишем Student.grade = grade + 1
    def grade(self, grade):
        self.__grade = grade



    def study(self, univer):
        print(f"{self.name}is in {univer}") # name наследует от Human и можем обращаться
        # из Human не можем залезать в класс Student, а наоборот можем





