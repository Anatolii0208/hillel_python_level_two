from sqlite3 import *

def cmp(str1, str2):
    str1 = [int(i) for i in list(str1[0].split('.'))]
    str2 = [int(i) for i in list(str2[0].split('.'))]
    com = 0
    if str1[2] > str2[2]:
        return True
    elif str1[2] < str2[2]:
        return False
    else:
        com = 1

    if (str1[1] > str2[1]) and com == 1:
        return True
    elif (str1[1] < str2[1]) and com == 1:
        return False
    else:
        com = 2

    if (str1[0] > str2[0]) and com == 2:
        return True
    else:
        return False

def oldest():
    cur.execute("""SELECT дата_выдачи
                            FROM table_2
                                """)
    list_d = list(cur.fetchall())

    for i in range(len(list_d) - 1):
        for j in range(len(list_d) - i - 1):
            if cmp(list_d[j],list_d[j + 1]):
                list_d[j], list_d[j + 1] = list_d[j + 1], list_d[j]
    ss = []
    ss.append(list_d[0][0])
    cur.execute("""SELECT *
                    FROM table_2
                        WHERE дата_выдачи == ?
                        """,ss)
    return cur.fetchall()

def yangest():
    cur.execute("""SELECT дата_выдачи
                            FROM table_2
                                """)
    list_d = list(cur.fetchall())

    for i in range(len(list_d) - 1):
        for j in range(len(list_d) - i - 1):
            if cmp(list_d[j],list_d[j + 1]):
                list_d[j], list_d[j + 1] = list_d[j + 1], list_d[j]
    ss = []
    ss.append(list_d[len(list_d) - 1][0])
    cur.execute("""SELECT *
                    FROM table_2
                        WHERE дата_выдачи == ?
                        """,ss)
    return cur.fetchall()

def sum_base():
    cur.execute("""SELECT сумма
                         FROM table_2""")

    list_d = cur.fetchall()
    sum1 = 0
    for i in list_d:
        sum1 += int(i[0])
    return sum1

def first_three():
    cur.execute("""SELECT *
                        FROM table_2
                            LIMIT 3""")
    return cur.fetchall()

def smaller():
    cur.execute("""SELECT *
                        FROM table_2
                        WHERE сумма > 999999
                            """)
    list_d = list(cur.fetchall())
    return list_d

n = input()
conn = connect(n) #Создание / Подключение к базе данных с указанным названием

#Создание объекта курсора (уникальный указатель на данные)
cur = conn.cursor()

with open("part_data_1.txt", "r", encoding="utf-8") as file:
    h = file.readline().split()
    table_1 = []
    for line in file.readlines():
        a = line.split()
        #print(a)
        if len(a) < 5:
            continue
        table_1.append(a)

cur.execute(f"""CREATE TABLE table_2
    ({str(h[0])}, {str(h[1])}, {str(h[2])}, {str(h[3])}, {str(h[4])})""")

for i in table_1:
    for j in range(len(i)):
        if i[j].isdigit() == True:
            i[j] = int(i[j])
    cur.execute("""INSERT INTO table_2
        VALUES(?,?,?,?,?)""",i)


print(sum_base())
print(first_three())
print(smaller())
print(yangest())
print(oldest())
conn.commit()

# Закрыть подключение
conn.close()