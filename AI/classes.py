#PEB8
#переменные some_pare...
#классы SomeClass
#функции some_function
class Human:#объявление класса Human
    def say_hello(self): #описание метода класса
        print('Hello!') #self = себя
    def say_this(self, messege):#мы можем передавать аргумент
        print(messege)#как в обычную функцию
    def hello(self):
        self.say_this("Hello my nigger!")



rick = Human() #создание объекта (сущности) класса Human
nick = Human()
dick = Human()
print(rick,nick,dick)

rick.say_hello()
nick.say_this("Hello yourself!")
dick.hello()