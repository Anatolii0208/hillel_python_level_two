"""from cities import *
cit1 = Cities("i",5,"u")
cit1.info()
print(dir(Cities))
"""
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self,n):
        if len(n) in range(1,50):
            self.__name = n
        else:
            self.__name = "Taras"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, n):
        if n in range(1, 100):
            self.__age = n
        else:
            self.__age = 50

class Student(Person):

    def dataInfo(self, course):
        print(self.name, self.age, course)
per = Student("oo",0)
per.name = "pp"
per.dataInfo("iii")
