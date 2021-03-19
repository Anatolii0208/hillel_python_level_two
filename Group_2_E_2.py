'''import random

#lists
# []
rft = "3rewf"
list_1 = list(rft)
print(list_1)

ap_1 = [rft]
print(ap_1)

list_2 = []

list_2 .append('43')
list_2 .append("r3efref")
list_2 .append("42.5")

print(list_2 )

list_2 .extend(list_1) #Добавление элементов списка fr как элементы списка ap
print(list_2 )

list_2.insert(10, "AAAA")
print(list_2 )
list_2.insert(10, "AAAA")
list_2.insert(10, "AAAA")

list_2.insert(-3, "33333")
print(list_2 )

list_2.insert(-12, "ZZZZZZZ")
print(list_2 )

#Удаление элементов
list_2.remove('AAAA')
print(list_2 )

list_2.pop(4)
print(list_2 )

print(list_2.index('AAAA')) #Указанный элемент ищет его индекс
#print(list_2.index('etgj34059tu5e')) Ошибка не существует в списке

print(list_2.count("AAAA")) #Количесвто элементов в списке


#list_2.sort()#Сортирует список и изменяет его
#print(list_2)

#list_2.sort(reverse=True)#Сортирует список и изменяет его
#print(list_2)

#list_3 = sorted(list_2) #Сортирует копию списка list_2 но не изменяет его
#print("list_2 = ", list_2)
#print("list_3 = ", list_3)

list_2.reverse()
print(list_2)
print( list_2.copy())
#list_2.clear()
#print(list_2)

#Анигиляция элементов списка
#del list_2[4]
#del list_2[4:]
#del list_2 #Анигиляция самого обьекта списка
#print(list_2)

#Lists slising

print(list_2[2:-1])
print(list_2[2:-1:2])
print(list_2[2::])
print(list_2[:5:2])

print(list_2[-5:-1])

#list comprehantion - списковые включения

#Поиск самого длинного элемента списка
len_max = ""
for i in range( len(list_2) ):
    if len(len_max) < len(list_2[i]):
        len_max = list_2[i]

print(f"Bigest element: {len_max} EEEEEEEE" )

len_max = ""
for e in list_2:
    if len(len_max) < len(e):
        len_max = e
print(f"Bigest element: {len_max} EEEEEEEE" )



#list comprehantion

list_4 = []
for i in range(10):
   list_4.append(random.randint(10))

list_5 = [random.randint(0, 10) for i in range(10)]
print(list_5)
list_6 = []

#classic
for e in list_5:
    if not e % 2:  # if e%2 == 0:
        list_6.append(e)

print(list_6)

list_7 = [elem for elem in list_5 if not e % 2]
print(list_7)'''

"""Создайте список из 20 элементов, элементы случайны (от 10 до 100)
Записать каждый 2й элемет этого списка в другой список
при этом возвести в квадрат(вторую степень) каждый взятый элемент"""

import random
list1 = [random.randint(10,100) for i in range(20)]
list2 = [el ** 2 for el in list1[::2]]

print(list1)
print(list2)
