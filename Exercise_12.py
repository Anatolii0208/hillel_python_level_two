from pack_1 import *
#from pack_1 import Person as P
#import pack_1 as p

per_1 = Person(s = "Taras", n = "", p = "AA435798")
per_2 = Person("Iliya", "Repin", "TT738742")
per_3 = Person("Petr", "Zaruba", "OO873495")

per_1.info()
print(per_1.name) #вызов геттер метода для переменной name
per_1.name = "Юрий" #Вызов сеттер метода для переменной name
#car_1 = Auto(input())

#Удаление обьекта класса
#del per_1
per_1.info()
per_2.info()
per_3.info()

#car_1.move(230)

#Инкапсуляция

