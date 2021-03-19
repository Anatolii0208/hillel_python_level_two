"""def sol(ed, le):
    #action
    return ed * ed, le * le


var_1, var_2 = sol(34, 12)

print(f"var_1 = {var_1}")
print(f"var_2 = {var_2}")
print(sol(34, 12))
"""
#Classic
"""
temp = var_1
var_1 = var_2
var_2 = temp
"""
#Operator ,
#Swap
"""
var_1 , var_2 = var_2, var_1

print(f"var_1 = {var_1}")
print(f"var_2 = {var_2}")
"""

#Функция с нeизвестным количеством параметров
"""def sel(*parms):
    sumP = 0
    for val in parms:
        if type(val) == type(int()):
            sumP+=val
        elif type(val) == type(list()):
            sumP += sum(val)
    return sumP
"""
#print(sel(4, 6, 65, 34, 23, [23, 34, 32,12 ,12, 43]))

#Область видимости или область действия


#Самая глобальная переменная
"""peremennaya = 101

def de():
    global peremennaya
    #Локальная область программы
    peremennaya = 2002
    print(f"{peremennaya} in fun")


if len(input("Vvedi chto-to: ")) > 10:
    sep = "Ledorub"
    peremennaya += 1000
    print(f"{sep}, The end for fun...")

print(peremennaya)
de()
print(peremennaya)

print("The End")
"""

from random import *
#import copy
#range(FINISH) == from 0 to FINISH step = 1
#range(START, FINISH) == from START to  FINISH step = 1
#range(START, FINISH, STEP) == from START to  FINISH step = STEP
#list_1 = [randint(1, 10) for i in range(10)]

#list_1.extend([2,2,2,2,2])

#print(f"list_1 = {list_1}")

#Удаление определенных элементов из списка
"""while 2 in list_1:
    list_1.remove(2)

print(list_1)
"""

#Копирование списков

#shallow copy - Быстрое копирование
"""list_2 = list_1

print(f"list_2 = {list_2}")

list_2.append(2222)

print(f"list_1 = {list_1}")
print(f"list_2 = {list_2}")
"""
#deep copy - Глубокое копирование
'''list_3 = copy.deepcopy(list_1)
print(f"list_1 = {list_1}")
print(f"list_3 = {list_3}")

list_3.append(44444)
list_1.pop(-1)
print(f"list_1 = {list_1}")
print(f"list_3 = {list_3}")
'''''
#Cheat Engine
"""
list_4 = list_1[:]

list_4.append(5555)
list_1.pop(-1)
print(f"list_1 = {list_1}")
print(f"list_4 = {list_4}")
"""

#Вложение списков
#list_HZ = [ [ randint(0, 10) for i in range(10)]  for i in range(10) ]
#print(list_HZ)

"""for val in list_HZ:
    for el in val:
        print(el, end=" ")
    print()

print(f"list_HZ[3][5] = {list_HZ[3][5]}")
"""

import sys
#TUPLE - КОРТЕЖИ - константный список

de = ("feed", 34, "sdf")
print(de)

de_1 = ("erewrw",)
print(de_1)


list_HZ = [  randint(0, 10)   for i in range(10) ]
de_2 = tuple(list_HZ)
print(de_2)

list_1 = list(de_2)
print(list_1)

print(de_2[1:6])

print(f"size list = {sys.getsizeof(list_HZ)}")
print(f"size tuple = {sys.getsizeof(de_2)}")



