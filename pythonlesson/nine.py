#Мета инфо о файле
"""with open("input_1.txt","r") as gg:
    print(gg.buffer)
    print(gg.closed)
    print(gg.encoding)
    print(gg.errors)
    print(gg.line_buffering)
    print(gg.mode)
    gg.mode="w"
    print(gg.mode)
    print(gg.name)
    print(gg.newlines)"""


#Позиция курсора в файле
"""with open("input_1.txt","r") as ff:
    print(ff.read(100))
    print(ff.tell())#функция определение позиции курсора в файле
    ff.seek(5000)#функция перемещает курсор на определенное количесто байт
    print(ff.read(100))
    ff.seek(0, 1)#0 - начало файла, 1 - текущая позицияб 2 - конец файла
    print(ff.tell())"""


#Подсчет количества слов в файле
"""with open("input_1.txt","r") as zz:
    rd = " "
    count_word = 0
    while rd != "":
        rd = zz.read(1)
        if rd in " " or rd in "\n":
            count_word += 1
    print(f"countWord(1_example) = {count_word}")

    zz.seek(0,0)

    print(f"countWord(2_example) = {len(zz.read().split())}")"""


#TXT
"""from random import *
dict_1 = { "name": "Vladimir", "surname": "Bulgakov", "title": "Master of Margarita"}
list_1 = [randint(0,10) for i in range(10)]"""


"""with open("dict_1.txt", "w") as kk:
    kk.write(str(list_1))
    kk.write(str(dict_1))"""


#CSV
"""from csv import *



list_2 = [
    ["Dir",r"user_1.py"],
    ["File",r"user_2.js"],
    ["Modul",r"user_3.cpp"]
]


with open("path.csv", "w", newline="") as ss:
    writer(ss).writerow(list_2)
    #writerow-in line, writerows-in some lines


with open("path.csv", "r", newline="") as ss:
    #print(reader(ss))
    for el in reader(ss):
        print(el[0],el[1])

"""


"""
users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]


with open("path.csv", "w", newline="") as ss:
    column=["name","age"]
    DictWriter(ss, fieldnames=column).writeheader()
    #writerow-in line, writerows-in some lines
    DictWriter(ss, fieldnames=column).writerows(users)


with open("path.csv", "r", newline="") as ss:
    #print(reader(ss))
    for el in DictReader(ss):
        print(el["name"],el["age"])

#image like txt file
with  open("/Users/bogdansandybin/Downloads/TOLIK_free-file.png" , "rb" ) as image:
    print(image.read())"""


#Home_Task
"""from csv import *


factory = {"It department":3, "Sales dep":4, "Prodaction dep":5, "Law dep":6, "Construction dep":7}
factory["It department"]+=1
factory["Cleaning dep"]=3
del factory["Law dep"]


with open('path.csv', 'w') as csv_file:
    writer = writer(csv_file)
    for key, value in factory.items():
       writer.writerow([key, value])


with open('path.csv','r') as csv_file:
    reader = reader(csv_file)
    factory = dict(reader)
    print(factory)"""