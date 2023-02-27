
class Cat:
    def __init__(self,name):
        self.__name = name # Свойства ИМЯ для оьекта класса Cat
        self.__age = 0     # Возраст кота     __- знак инкапсуляции(не можем менять внутри)
    def set_age(self,age):
        if 1<=age<=25:
            self.age = age
        else:
            print("Ты лох")
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name





    def display_info(self):
        print(f"My name is {self.__name}, my age is {self.__age}.")


'''simons_cat = Cat("Rick")
print(simons_cat)
print(simons_cat.name, simons_cat.age)
print(type(simons_cat.name), type(simons_cat.age))

simons_cat.family = "Simpsons"
print(simons_cat.family)

simons_cat.display_info()

# the_age=int(input("Введите новый возраст кода:"))
# simons_cat.age += the age

simons_cat.set_age(25)
# simons_cat.age += 10 - Так нехорошо
print(simons_cat.name, simons_cat.age)'''

simons_cat = Cat("Nick")
print(simons_cat.get_age(),simons_cat.get_name())
simons_cat.display_info()

simons_cat.name = ("Dick")
print(simons_cat.get_name())




