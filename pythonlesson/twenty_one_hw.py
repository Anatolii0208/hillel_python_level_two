from sqlite3 import *

con = connect("Companies.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Storage_1(
    Tehnology TEXT,
    Company_name TEXT,
    Langvige TEXT,
    Number INTEGER 
)""")

#чтение файла
with open("Input_1 (1).txt","r") as file:
    list_d = list(file.read().split("\n"))
    list_a = []
    for i in list_d:
        list_near = list(i.split("\t"))
        if '+' in list_near[len(list_near) - 1]:
            list_near[len(list_near) - 1] = list_near[len(list_near) - 1][0:len(list_near[len(list_near) - 1]) - 1]
        list_a.append(list_near)


#Создание таблицы в бд
for i in list_a:
    cur.execute("""INSERT INTO Storage_1
                                    VALUES(?,?,?,?)""",
                i)
    con.commit()

#1. Реализовать подсчет количества уникальных Проектов - Типа на чем они написаны Delphi 7.0 и другие
cur.execute("""SELECT Langvige, COUNT(Langvige)
                    FROM Storage_1
                    GROUP BY Langvige
                    """)

#2. Найти все проекты которые имеют 1500 и более поинтов
cur.execute("""SELECT *
                    FROM Storage_1
                    WHERE Number >= 1500
                    """)

#3. Найти все проекты где БД создана в (Access) Например вот эта часть (ADO + Access) подходит
cur.execute("""SELECT Company_name
                FROM Storage_1
                    WHERE INSTR(Company_name,'(ADO + Access)') >= 1 
""")

#4. Найти компанию заказчика с самым длинным названием и подсчитать сколько эта компания делала заказов (то есть есть ли еще проекты сделанные для этой компании)
#Сортирует по длине названия компании
cur.execute("""SELECT Company_name
                    FROM Storage_1
                    ORDER BY LENGTH(Company_name)
                    """)

#Последний кортеж этого списка и будет с компанией с максимально длиной
MAX_LENTH = cur.fetchall()[len(cur.fetchall())-1][0]

#считаем количество проэктов с таким названием
cur.execute("""SELECT COUNT(Company_name)
                    FROM Storage_1
                    WHERE Company_name = ?
                    """,(MAX_LENTH,))


#5. Подсчитать количество компаний у которых количество поинтов не больше 800 и более 2220
cur.execute("""SELECT *
                    FROM Storage_1
                    WHERE Number <= 800 OR Number > 2220
                    """)

'''for el in cur.fetchall():
    print(el)'''

con.close()