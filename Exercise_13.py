from Cities import *
import random

cit_1 = Cities("Kontantinopol", "Estern Rome Empire", 1789549)
cit_2 = Cities("Dallas",  19549)

cit_1.getInfo()
cit_2.getInfo()

cit_3 = Cities()
cit_3.getInfo()

print(dir(Cities))
cit_4 = Cities( c = "Ukraine", count = 23423, n="Kiev" )
cit_4.getInfo()

#print('rhioirhfw')

#Создание обьекта класса Cities()
#cit_5 = Cities()
#Вызов внутреннего класса LOL() и его метода getInfo()
#cit_5.LOL().getInfo()

#Создание обьекта класса LOL() который находится в классе Cities
#cit_5 = Cities().LOL()
#cit_5.getInfo()
#res = random.Random()

#print(dir(res))

#Hacледование class
class Person:
    def __init__(self, n, a):
        #Инкапсулированые атрибуты
        self.name = n
        self.age = a

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if len(n) in range(1,50):
            self.__name = n
        else:
            self.__name = "Taras"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, OLOLO):
        if OLOLO in range(1, 100):
            self.__age = OLOLO
        else:
            self.__age = 50

class Student(Person):
    def dataInfo(self, course = "Python level 2"):
        print(f"name student = {self.name}, age = {self.age} by course {course} ")


student_1 = Student("Lisa", 21)
student_1.dataInfo("C++ Intro")