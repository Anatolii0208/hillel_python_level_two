from random import *
import sys
'''
lister = ["aew" for i in range(randint(5, 15))]

str_1 = ""

str_1 = "\n".join(lister)

print(str_1)
'''
#Обьявлление  и создание словарей
#rt = { ключ1 : значение1, ключ2 : значение2}

#ref = {"name" : "Vasya", "age" : 23, "sex" : "male"}
#print(ref["name"])

#ref = {1 : "Vasya", 2 : 23, 0 : "male"}
#print(ref[0])

#liste = [1 ,3 , 5, 53 , 'Lager', 23.43]
#print(liste[2])

#ref = {"name" : "Vasya", "age" : 23, "sex" : "male", "name": "Igor", "name":"Vika"}
#print(ref["name"])
#print(ref)

#dict_1 = {} #Словарь ТОЛЬКО СЛОВАРЬ

#liste = [ ["rfww" , 454 ],
#          ["rfwe", 342 ],
#          [234, "fewfw"]]

#tuple_1 = ( ("rfww" , 454 ),
#            ("rfwe", 342 ),
#            (234, "fewfw"))


#dict_2 = dict(tuple_1)
#print(dict_2)

#Использование элементов
'''user = {"+380965464582" : "Renat",
        "+380976964293" : "Olya",
        "+380987823478" : "Artem"}

print(user["+380976964293"])
user["+380976964293"] = "Diyna"
print(user)

user["+3806609230343"] = "Angor"
print(user)
'''

#Перебор элементов словаря
user = {"+380965464582" : "Renat",
        "+380976964293" : "Olya",
        "+380987823478" : "Artem"}
#for key in user:
#    print(key ,user[key])

#Базовый функционал
#Получение элемента по ключу
#print(user.get("+380976964293", "Unknown key"))
#print(user["+380976964123"])

#Удаление элементов
#pop
#user.pop("+380976964293", "Незя удалить его нет в словаре")
#del
#del user["+380976964123"]
#clear
#user.clear()

#Копирование и обьединение словарей
user_1 = {1 : "Jupiter",
        3: "Earth",
        10 : "Mercuri"}
#Update
#user_1.update(user)

#Lite Copy поверхностное копирование (по факту две переменные будут указывать на одни и теже данные)
#user_1 = user
#user_1.clear()
#print(f"user_1 = {user_1}")
#print(f"user = {user}")

#Deep Copy полное копирование
#user_1 = user.copy()
#user_1.clear()
#print(f"user_1 = {user_1}")
#print(f"user = {user}")

#Перебор словаря с помощью методом items
'''for key in user:
    print(key ,user[key])

for key, val in user.items():
    print(f"key = {key} val = {val}")

print(user.items())
'''

#Перебор ключей словаря keys
#print(user.keys())
#list_1 = set(user.keys())
#print(list_1)

#Перебор значений словаря values
#print(user.values())
#list_1 = list(user.values())
#print(list_1)
#print("\n".join(user.values()))

#Вложеность в словарях
'''
user = { "Zina" : {"phone" : "+3809946546167", "email" : "zina@gmail.com" },
"Evgenij" : {"phone" : "+380999379992", "email" : "zeka@gmail.com" , "telegramm" : "@zeka777"},
"Mihail" : [1, 3, 4, 0,6, 7],
}
'''
#print(user["Zina"]["email"])

#user_1 = { (4, 3, 2, 11) : {"phone" : "+3809946546167", "email" : "zina@gmail.com" } }
#print(user_1[(4, 3, 2, 11)])


# 1. Создать любой словарь, например города и страны их расположения или наоборот,
# потом создать функцию которая подсчитает количество ключей в этом словаре

#fr = {"Ukraine": "Kiev", "Estonia":"Tallin", "Bulgaria": "Sophia", "Turkey": "Ankara"}
#print(len(fr))

# 2. Создать словарь ключами которого будут названия чисел, а элементами целые значения этих чисел ( "Двадцать два" : 22),
# И необходимо вывести все числа которые больше 10 (формат вывода не важен).
'''
def me(e):
    return [ val for val in e.values() if val > 10 ]

fr = {"Триста": 300, "Двадцать два":22, "Семь": 7, "Один": 1}
print(me(fr))
'''
# 3. Применить словарь из предыдущего задания (Задание 2) и модифицировать
# его таким образом чтобы ключи стали элементами, а элементы ключами ( "Двадцать два" : 22) = (   22 : "Двадцать два")
def mu(e):
    res = {}
    for key, val in e.items():
        res[val] = key
    return res

ft = {"Триста": 300, "Двадцать два":22, "Семь": 7, "Один": 1}
print(mu(ft))
#В единственной строке записан текст.
# Для каждого слова из данного текста подсчитайте,
# сколько раз оно встречалось в этом тексте ранее.
#Словом считается последовательность непробельных символов идущих подряд, слова разделены
# одним или большим числом пробелов или символами конца строки.
