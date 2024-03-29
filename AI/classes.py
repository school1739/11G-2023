class Human:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class Student(Human):
    def __init__(self, name):
        super().__init__(name)
        self.__grade = 0

    def study(self, univer):
        print(f"{self.name} is in {univer}")

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade


student1 = Student("Rick")
rick.study("МАИ")
print(rick.grade)
rick.grade += 1
print(rick.grade)
