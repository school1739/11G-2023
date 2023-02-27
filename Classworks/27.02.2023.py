# Classwork. Lesson 2

# Конструктор
class Cat:
    def __init__(self, name):
        self.__name = name  # Свойство ИМЯ для объекта класса Cat
        self.__age = 0  # __ - знак икапсуляции

    def set_age(self, age):
        if 1 <= age <= 25:
            self.age = age
        else:
            print("Ты лошара (С) Roni")

    def display_info(self):
        print(f"My name is {self.name}, my age is {self.age}.")



'''...'''



simons_cat = Cat("Rick")
print(simons_cat.name, simons_cat.age)
print(type(simons_cat.name), type(simons_cat.age))

simons_cat.family = "Simpsons"
print(simons_cat.family)
simons_cat.display_info()

simons_cat.set_age(30)
print(simons_cat.name, simons_cat.age)







#Калантарян Мери и Нечаев Серигей