'''class Human: # Создаем новый класс
    def __init__(self, name): # Конструктор
        print(f'Родился человек с именем {name}!') # Сообщение о создании сущности
        self.__name=name # Инкапсулирование(__) свойства
        self.__age=0
        self.__health=100

    @property # Начало GETTER (получатель/возвращатель)
    def age(self):
        return self.__age
    @age.setter # Начало SETTER (установитель/определитель) Свойства
    def age(self, new_age):
        if 1<new_age<100:
            self.__age=new_age
        else:
            print('Fuck off.')

class Student(Human): # подкласс студент
    def school(self):
        self.school=1739
        print(1739)


male_1=Human('Rick')
female_1=Human('Doro')
print(male_1.age())
male_1.set_age(15)
print(male_1.age())
print(male_1.age)

male_1.age=15
print(male_1.age)'''

"""# Все руками
class Human:
    def __init__(self,name):
        print(f'Родился человек с именем {name}!')
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
class Student(Human):
    def study(self,univer):
        print(f"{self.name} учится в {univer}")
        self.__grade = 0

    def __init__(self, name):
        super().__init__(name)
    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self,grade):
        self.__grade=grade







rick = Student("Rick")
rick.study("МГУ")
rick.grade+=1
print(rick.grade)"""





