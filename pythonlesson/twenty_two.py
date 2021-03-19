import sys

#1. С помощью lambda извлеките из списка числа, делимые на 15.
list_example = [11,15,30,34,43,56,45,30]
list_d = list(map(lambda a: a if a % 15 == 0 else None , list_example))
[print(i,end = ' ') for i in list_d if i != None]
print()
#2.Cоздать рекурсивную функцию которая проверит, все ли числа в последовательности уникальны. Если нет то вернуть false если уникальны то вернуть true.
def uniq(list_1):
    list_1.sort()
    if len(list_1) == 1:
        return True
    return list_1[0] != list_1[1] and uniq(list_1[1:])

#3. Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором, решить рекурсивно.
def uniq2(list_1, list_2):
    if len(list_1) == 0:
        return 0
    if list_1[0] not in list_2:
        print(list_1[0],end=" ")
    list_1 = list_1[1:]
    uniq2(list_1,list_2)

#4. Принимаем от пользователя последовательность чисел, разделённых запятой. Составить список и кортеж с этими числами, рекурсивно.
#Для списка
def coma(str_coma):
    global b
    if len(str_coma ) == 1:
        b.append(str_coma[0])
        print(b)
        return 0
    b.append(str_coma[0])
    coma(str_coma[2:])

#4. Принимаем от пользователя последовательность чисел, разделённых запятой. Составить список и кортеж с этими числами, рекурсивно.
#Для кортежа
def coma_2(str_coma):
    global a
    if len(str_coma ) == 1:
        a = list(a)
        a.append(str_coma[0])
        a = tuple(a)
        print(a)
        return 0
    a = list(a)
    a.append(str_coma[0])
    a = tuple(a)
    coma_2(str_coma[2:])
#5. Найдите рекурсивно три ключа с самыми высокими значениями в словаре myDict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.
def three_max_dict(dict_1):
    global u
    if u == 3:
        return 0
    u+=1
    list_keys = list(dict_1.values())
    max1 = max(list_keys)
    for i,j in dict_1.items():
        if j == max1:
            print(i,end = " ")
            dict_1.pop(i)
            break
    return three_max_dict(dict_1)

str_1 = "1,2,3,4,5,6,7,8"
t = [1, 3, 5, 7, 3, 9]
myDict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
p = [5, 10, 7, 3, 7]
a = ()
b = []
u = 0
print(uniq(t))
uniq2(t,p)
print()
coma(str_1)
coma_2(str_1)
three_max_dict(myDict)
