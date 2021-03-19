"""код_договора	код_клиента	код_кредита	дата_выдачи	сумма
1	ItSorce	23	04.10.2018	1000000
2	—odewars	3	17.01.2019	20000
3	ItCraft	17	31.12.2017	340000
4	SoftVerse	1	25.07.2020	900000
5	ItLand	44	06.06.2016	3000000
6		22	11.08.2011	440000
7	PostCode	22		830000
8	CraftSource	13	31.12.2017	340000
9	SoftVerse	1	25.07.2020	900000
10	ItCraft	17	31.12.2017	340000
"""
from copy import deepcopy
from sqlite3 import *

n = input()
conn = connect(n) #Создание / Подключение к базе данных с указанным названием

#Создание объекта курсора (уникальный указатель на данные)
cursor = conn.cursor()

with open("part_data_1.txt", "r", encoding="utf-8") as file:
    h = file.readline().split()
    table_1 = []
    for line in file.readlines():
        a = line.split()
        #print(a)
        if len(a) < 5:
            if a[0].isdigit() == False:
                a.insert(0,'')
            if a[1].isdigit() == True:
                a.insert(1, '')
            if a[2].isdigit() == False:
                a.insert(2, '')
            if a[3].isdigit() == True:
                a.insert(3, '')
            if a[4].isdigit() == False:
                a.insert(4, '')
        table_1.append(a)
cursor.execute(f"""CREATE TABLE table_1
    ({str(h[0])}, {str(h[1])}, {str(h[2])}, {str(h[3])}, {str(h[4])})""")
table_2 = deepcopy(table_1)
for i in table_1:
    cursor.execute("""INSERT INTO table_1
        VALUES(?,?,?,?,?)""",i)

#second table
cursor.execute(f"""CREATE TABLE table_2
    ({str(h[0])}, {str(h[1])} UNIQUE, {str(h[2])}, {str(h[3])}, {str(h[4])})""")
j=1
for i in table_1:
    #print(table_1_help)
    try:
        cursor.execute("""INSERT INTO table_2
            VALUES(?,?,?,?,?)""",i)
    except IntegrityError:
        i[1] = 'hillel'+str(j)
        j+=1
        cursor.execute("""INSERT INTO table_2
            VALUES(?,?,?,?,?)""", i)
#third table
cursor.execute(f"""CREATE TABLE table_3
    ({str(h[0])}, {str(h[1])}, {str(h[2])} , {str(h[3])} NOT NULL, {str(h[4])})""")
for i in table_2:
    #print(table_1_help)
    if i[3] == '':
        print("You write some incoret inputs")
        continue
    cursor.execute("""INSERT INTO table_3
        VALUES(?,?,?,?,?)""",i)
conn.commit()

# Закрыть подключение
conn.close()