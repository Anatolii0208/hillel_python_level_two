from random import *

#HomeW_1
'''
str_1 = input("Введите строку: ")
str_1.replace(" ", "")

if str_1.lower() in str_1[::-1].lower():
    print("This is polindrome")
else:
    print("This is NOT polindrome")
'''

#HomeW_2
'''
#2_1
as_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([val for val in as_1 if val < 5])

#2_2
as_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ba = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print([val for val in as_1 if val in ba])

#2_3
arr = [6, 6, 2, 1, 5, 8, 13, 21, 34, 55, 89]
bar = [1, 18, 3, 4, 5, 9, 7, 8, 9, 10, 11, 12, 13]
res = []
[res.append(val) for val in arr if not val in bar and not val in res]
[res.append(val) for val in bar if not val in arr and not val in res]
print(res)
'''

#HomeW_3
#3_1
'''
def evenMax(lister):
    return max( [val for val in lister if not val % 2] )
list_1 = [randint(1, 50) for i in range(randint(5, 20))]
print(list_1)
print(f"Max even elem: {evenMax(list_1)}")
'''

#3_2
'''
def threeMax(l):
    l.sort(reverse = True)
    return l[:3]

list_1 = [randint(1, 50) for i in range(randint(5, 20))]
print(list_1)
print(f"Max three: {threeMax(list_1)}")
'''

#3_3
'''
def evenChecker(l_1, l_2):
    return len([val for val in l_1 if not val % 2]) > len([val for val in l_2 if val % 2])

list_1 = [randint(1, 50) for i in range(randint(5, 20))]
list_2 = [randint(1, 50) for i in range(randint(5, 20))]
print(list_1, "\n", list_2)
print(f"Max three: {evenChecker(list_1, list_2)}")
'''

#HomeW_4
'''
def sor(*param):
    summ = 0.0
    for val in param:
        if type(val) == type(int()) or type(val) == type(float()):
            summ += val
        elif type(val) == type(list()) or type(val) == type(tuple()):
            summ += sum(val)
    return summ

print(sor(34, 11, 23.23, [3, 5, 6,32, 23], (4, 3, 2, 23, 5, 5, 5), 43, 111) )
'''
import sys

#set () - Множества, может хранить только уникальные элементы
us = set()
list_1 = [randint(1, 10) for i in range(randint(5, 20))]
print(f"list = {list_1}")
us = set(list_1)
print(f"Set = {us}")

er = {"For", "Lor", "For", "Aggr"}
print(f"Set = {er}")

print(sys.getsizeof(us))
print(sys.getsizeof(list_1))


'''list_2 = [randint(1, 10) for i in range(randint(5, 20))]
list_3 = [randint(1, 10) for i in range(randint(5, 20))]
print(f"list_2 = {list_2}")
print(f"list_3 = {list_3}")
res = list(  set(list_2 + list_3 )  )
print(res)
'''

#Добавление элемента
us.add(23)
print(us)
#Delete element
us.remove(23)
print(us)

us.discard(101)
print(us)

#us.clear()#удаляет элементы но не обьект
#del us #Анигиляция множества

#обьеденения множества
#res= set_1.union(set_2)

#Пересечение множеств
# res = set_1.intersection(set_2) #Вязятие элементов присутствующих в обоих множествах
# res = set_1 & set_2

#Вычитание множеств
#res = set_1.difference(set_2)

#Определения присустствия одного множества как части другого
#issubset()

#Обратное действия #issubset()
#issuperset()


set_1 = set([1,2,3])
set_2 = set([randint(1, 10) for i in range(randint(5, 20))])
print(f"Set_1 = {set_1}")
print(f"Set_2 = {set_2}")
print(f"Unic elen from set_1: {set_1.issuperset(set_2)}")

#FROZEN SET - константное множество
set_3 = set([randint(1, 10) for i in range(randint(5, 20))])
fset_4 = frozenset([randint(1, 10) for i in range(randint(5, 20))])
print(f"Set_3 = {set_3}")
print(f"FSet_4 = {fset_4}")
print(sys.getsizeof(set_3))
print(sys.getsizeof(fset_4))