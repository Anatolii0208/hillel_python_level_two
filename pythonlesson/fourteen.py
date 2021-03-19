#Наследование

class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    #property
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, n):
        if n in range(1, 100):
            self.__age = n
        else:
            self.__age = 20

    def displayInf(self):
        print(f"Name: {self.name}, \tAge: {self.__age}")


class Employee(Person):
    def __init__(self, name, age, fact):
        Person.__init__(self, name, age)
        self.factory = fact

    def displayInf(self):
        Person.displayInf(self)
        print(self.factory)

    def empQuality(self):
        return 345


class Student(Person):
    def __init__(self, n, a, uni):
        Person.__init__(self, n, a)
        self.univer = uni
        self.name = n

    @property
    def name(self):
        return self.__name + "behelor"

    @name.setter
    def name(self, n):
        self.__name = n

    def displayInf(self):
        Person.displayInf(self)
        print(f"Name university: {self.univer}")


"""emp = Employee("Greg", 32)
emp.metaData("lll")
emp.age = 31
emp.displayInf()

stu = Student("Petr", 18, "youtube")
stu.displayInf()
spisok = [Employee("Lora", 27, "Googl") ,
          Student("Zina", 19, "HNEU"),
          Person("Alexandr_1", 100500),
          Employee("Ghoul", 44, "Microsoftina") ]

spisok[0].displayInf()
print(spisok[1].name)

for obj in spisok:
    if isinstance(obj, Employee):
        print(obj.empQuality())
    elif isinstance(obj, Student):
        print({obj.univer})


    print(issubclass(Person, Student))
    obj.displayInf()

"""


#строковое предстовление объекта
epm = Person("Egor", 34)

print(epm)