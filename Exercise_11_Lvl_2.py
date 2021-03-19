#Основные модули языка пайтон
#import random #подключить весь модуль рандом
#from random import randint, random #выборочное подключение элементов модуля рандом
#from random import * #Подключение всех элементов модуля

#randint() - случайое целое число
#print(randint(-100, 250))

#random() - случайое вещественное число от 0.0 до 1.0
#print(random())

#randrange() - случайное целое число из набора
#print(randrange(34))
#print(randrange(1,34))
#print(randrange(5,34, 2))

#for i in range(10):
#    print(randrange(1, 34, 2), end= " ")

#choice() - выбирает случайный элемент из списка
#list_1 = [randint(1,50) for i in range(randint(5,20))]
#print(list_1)
#print(choice(list_1))

#shuffle() - функция которая перемешивает элементы перечисляемого обьекта
#list_1 = [ str(randint(1,50)) for i in range(randint(5,20))]
#print(list_1)
#shuffle(list_1)
#print(list_1)

#from math import *

#pow() ** - возведение числа в степень
#sqrt(number) - квадратный корень числа number

#ceil(number) - округление числа до ближайшего наибольшего целого
#print(ceil(3.000000000000001))

#floor(number) - округление числа до ближайшего наименьшего целого
#print(floor(3.99))

#factorial(number) - факториал числа

#cos()
#sin()
#radians()

#from locale import *

#setlocale()
#LC_ALL - применяет локализацию ко всем единицам измерения категорий (дата, время, валюта...)
#LC_NUMERIC - локализация чисел
#LC_MONETARY - локализация валют
#LC_TIME - локализация время и даты
#LC_CTYPE - локализация алфавитов
#LC_COLLIATE - применение локализации к сравнению строк

#setlocale(LC_ALL, "us")
"""
num = 23423.89234
formnum = format_string("%f", num)
print(formnum)

formnum_1 = format_string("%.2f", num)
print(formnum_1)

formnum_1 = format_string("%d", num)
print(formnum_1)

money = 345.34
print(currency(money))
"""

'''from decimal import *

num = 0.01 + 0.1 + 0.1
print(num)

num = Decimal("0.1")
num = num + num + num
print(num)


num = Decimal("0.10")
num = num + num + num
print(num)

sol = Decimal("0.83138")
print( float(sol.quantize(Decimal("1.000"), ROUND_HALF_UP)))
'''

class Animal:
    animalClass = "Ссавцы"
    animalType = "Тигр"
    age = 23

    def run():
        print("Animal RUNNNN!!")

anim_1 = Animal
anim_1.run()

print(anim_1.animalClass)
anim_1.animalClass = "TROLOLOLO"
print(anim_1.animalClass)