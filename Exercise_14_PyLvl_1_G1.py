from random import *

#Списковое включение
list_1 = [ randint(1, 20) for i in range(10) ]
print(f"Before sort list = {list_1}")
countSwap = 0
countIter = 0
#Selection sort
for i in range(len(list_1)):
    #Минимальный элемент на текущем шаге
    min_elem = i

    #Цикл для перебора не отсортированых элементов
    #range (START, BEFORE_FINIST)
    for j in range(i+1, len(list_1)):
        if list_1[j] < list_1[min_elem]:
            min_elem = j

        countIter += 1

    #Вставка минимального элемента на первую позицию текущей части списка
    list_1[i], list_1[min_elem] =  list_1[min_elem],  list_1[i]
    countSwap += 1
    #temp = list_1[i]
    #list_1[i] = list_1[min_elem]
    #list_1[min_elem] = temp

print(f"Sorted list = {list_1}")
print(f"countIter = {countIter}")
print(f"countSwap = {countSwap}")

#Insertion sort
list_1 = [ randint(1, 20) for i in range(10) ]
print(f"Before sort list = {list_1}")
countSwap = 0
countIter = 0

for i in range(1, len(list_1)):
    #Запоминаем для вставки
    item_ins = list_1[i]
    #Запоминаем индекс предыдущего элемента
    before_elem = i - 1
    #Будем перемещать элементы вперед(слева на право) по списку
    #если они больше чем item_ins (элемент для вставки)
    #range (START, BEFORE_FINIST)
    while before_elem >= 0 and list_1[before_elem] >  item_ins:
        list_1[before_elem + 1] = list_1[before_elem]
        before_elem -= 1
        countIter += 1

    #Вставка минимального элемента на первую позицию текущей части списка
    list_1[before_elem + 1] =  item_ins
    countSwap += 1

print(f"Sorted list = {list_1}")
print(f"countIter = {countIter}")
print(f"countSwap = {countSwap}")

#Встроенные методы сортировки

#Quick sort
list_1 = [ randint(1, 20) for i in range(10) ]
print(f"Before sort list = {list_1}")

#Изменяет базовый список который ее вызывает
list_1.sort(reverse=True)
print(f"Sorted list = {list_1}")

#Модификация Quick sort
list_1 = [ randint(1, 20) for i in range(10) ]
print(f"\n\nBefore sort list = {list_1}")
#НЕ ИЗМЕНЯЕТ базовый список который ее вызывает
print(f"Sorted list = {sorted(list_1, reverse=True)}")
print(f"After sort list = {list_1}")


#Найти два максимальных и два минимальных списка
list_1 = [ randint(1, 20) for i in range(10) ]

list_1.sort()
print(f"\n\nBefore sort list = {list_1}")
print(f"min elem_1 = {list_1[0]}  min elem_2 = {list_1[1]}")
print(f"MAX elem_1 = {list_1[-1]}  MAX elem_2 = {list_1[-2]}")

#Найти center ЭЛЕМЕНТ списка
#НАйти среденее ЗНАЧЕНИЕ списка

list_1 = [ randint(1, 20) for i in range(randint(5, 20)) ]
print(f"Before sort list = {list_1}")
#Нашли средний элемент списка
if len(list_1) % 2:
    print(f"centr elem = {list_1[len(list_1) // 2]}")
else:
    print(f"centr elem = {list_1[len(list_1) // 2 - 1: len(list_1) // 2 + 1]}")

sum_1 = 0
for el in list_1:
    sum_1 += el

print(f"middle val = {sum_1 // len(list_1)}")

#Cheat engine METHOD
print(f"middle val = {sum(list_1) // len(list_1)}")