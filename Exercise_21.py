#15
# class Animals:
#     def __init__(self, n, w, teat):
#         self.__name = n
#         self.weght = w
#         self.__type_eat = t
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         if len(n) >= 2:
#             self.__name = n
#         else:
#             self.__name = "Абу"
#
#     @property
#     def weight(self):
#         return self._weight
#
#     @weight.setter
#     def weight(self, n):
#         if n >= 1:
#             self.__weight = n
#         else:
#             self.__weight
#
#     @property
#     def type_eat(self):
#         return self.__type_eat
#
#     def getInf(self):
#         return f"{self.name}, {self.__type_eat}, кол-во потребляемой еды: {self.weight}"
#
# class Predator(Animals):
#     def __init__(self, name, weight):
#         Animals.__init__(self, name, weight, "Predator")
#
# class Herb(Animals):
#     def __init__(self, name, weight):
#         Animals.__init__(self, name, weight, "Herb")
#
# class Omni(Animals):
#     def __init__(self, name, weight):
#         Animals.__init__(self, name, weight, "Omni")
#
# animals = [
#     Predator("Lion", 150),
# Predator("Jaguar", 100),
# Predator("Tiger", 175),
# Herb("Cow", 500),
# Herb("Elephant", 500)
# Herb("Apex", 500),
# Omni("Pig", 200),
# Omni("Bear", 400),
# Omni("Manky", 30)
# ]
# #15_1
# #Classic
# def sorFood(spisok):
#     for i in range(len(spisok)):
#         for j in range(len(spisok) + 1 - i):
#             if spisok[j].weight > spisok[j + 1].weight:
#                 spisok[j], spisok[j + 1] = spisok[j + 1], spisok[j]
#             elif spisok[j].weight == spisok[j + 1].weight:
#                 if spisok[j].name < spisok[j + 1].name:
#                     spisok[j], spisok[j + 1] = spisok[j + 1], spsok[j]
#     return spisok

#
# for el in sorFood(animals):
#     print(el.getInf())

#Copmre
# def getItem(item):
#     return (item.weight, item.name)
#
# animals.sort(key=getItem, reverse=True)
#
# for el in animals:
#     print(el.getInf())
""""""
#15_2

# for el in animals[:5]:
#     print(el.getInf())

#15_3
# for el in animals[-3:]:
#     print(el.name)


#15_4
# from csv import *
# with open("animals.csv", "w") as file:
#     colum = ["Name", "Weight", "Type_eat"]
#     DictWriter(file, fieldnames= colum).writeheader()
#
#     temList = [{ "Name" : el.name, "Weight" : el.weight, "Type_eat" : el.type_eat }  for el in animals]
#     DictWriter(file, fieldnames=colum).writerows(temList)
#
# with open("animals.csv", "r") as file:
#     for el in DictReader(file):
#
""""""

#16
# from sqlite3 import *
#
# data = []
#
# with open("part_data_1.txt", "r") as file:
#     header = file.readline().split()
#
#     for el in file.readlines():
#         data.append(el.split())
#
# # print(header)
# # print(data)
#
#
# db = input("Name for DB:")
# con = connect(db)
# cur = con.cursor()
#
# cur.execute(f"""CREATE TABLE IF NOT EXISTS Tb_1
# ({header[0]} INTEGER PRIMARY,
# {header[1]} NVARCHAR(30) UNIQUE,
# {header[2]} INTEGER NOT NUL,
# {header[3]} NVRACHAR(15),
# """)
# con.commit()
#
# for el in data:
#     if len(el) == 5:
#         try:
#             cur.execute("""INSERT INTO Tb_1
#             VALUES(?,?,?,?,?)""", tuple(el))
#         except IntegrityE as er:
#             print("Error# UNIQUE")
#         else:
#             con.commit()
#

""""""
#17
from sqlite3 import *

data = []

with open("part_data_1.txt", "r") as file:
    header = file.readline().split()


# print(header)
# print(data)


db = "dbLol3D"
con = connect(db)
cur = con.cursor()

cur.execute(f"""CREATE TABLE IF NOT EXISTS Tb_1
({header[0]} INTEGER PRIMARY KEY,
{header[1]} NVARCHAR(30),
{header[2]} INTEGER NOT,
{header[3]} NVRACHAR(15)
{header[4]} MONEY)
""")
con.commit()

for el in data:
    if len(el) == 5:
        try:
            cur.execute("""INSERT INTO Tb_1
            VALUES(?,?,?,?,?)""", tuple(el))
        except IntegrityError as er:
            print("Error# UNIQUE")
        else:
            con.commit()

#17_1
cur.execute("""SELECT * 
                FROM Tb_1
                    LIMIT 3""")

#17_2
cur.execute("""SELECT SUM(сумма) 
                FROM Tb_1""")

#17_3
cur.execute("""SELECT * 
                FROM Tb_1
                    WHERE сумма > 999999""")
#17_4
cur.execute("""SELECT * 
                FROM Tb_1""")

# for el in cur.fetchall():
#     print(el)
from datetime import *

def getDateTime(el):
    el[3] =  datetime.strptime( el[3], "%d.%m.%Y")
    return el

spisok = [ (list(el)) for el in cur.fetchall() ]
print(spisok)

oldData = datetime.now()
credit = []

for el in spisok:
    if el[3].year != oldData.year:
        oldData = el[3]
        credit= el
    elif el[3].year != oldData.year:
        if el[3].month != oldData.month:
            oldData = el[3]
            credit = el
        elif el[3].month != oldData.month:
            if el[3].day < oldData.day:
                oldData = el[3]
                credit= el
print(oldData)
print(credit)


for el in spisok:
    if el[3].year < oldData.year:
        oldData = el[3]
    elif el[3].year() == oldData.year:
        if el[3].month() < oldData.month:
            oldData = el[3]
        elif el[3].month == oldData.month:
            if el[3].day < oldData.day:
                oldData = el[3]
print(oldData)
con.close()

