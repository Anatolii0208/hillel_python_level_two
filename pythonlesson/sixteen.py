from sqlite3 import *

#объект коонекта
conn = connect("Exercise_DB.db") #Создание / Подключение к базе данных с указанным названием

#Создание объекта курсора (уникальный указатель на данные)
cursor = conn.cursor()

#Создание таблици
"""
CREATE TABLE name_table
    (name_column_1, surname_column_2, age_column_3)
"""
#cursor.execute("""CREATE TABLE Person
#   (name, surname, age)""")

#Типы данных
#TEXT - обычная строка
#INTEGER - целый тип данных
#FLOAT - вещественный тип данных
#BLOB - большие бинарные файлы
#BIT - 0 / 1 логический тип данных
#MONEY - тип данных для хранениея денежных едениц
#NVARCHAR - хранит данные в unicode

#cursor.execute("""CREATE TABLE Table_2
#  (userName NVARCHAR(20), email NVARCHAR(30), phone NVARCHAR(20), age INTEGER)""")

#Запрос на удаление таблицы
#cursor.execute("""DROP TABLE Person""")

# Переименование таблицы
#cursor.execute("""ALTER TABLE Table_2 RENAME TO Account """)

#Типы ограничений
    #Настройка главного ключа
#cursor.execute("""CREATE TABLE Table_2
 #    (id INT PRIMARY KEY,
  #   userName NVARCHAR(20),
   #  email NVARCHAR(30),
    # phone NVARCHAR(20),
     #age INTEGER)""")
    #Настройка точки отсчета для поля
#cursor.execute("""CREATE TABLE Table_3
 #    (id INTEGER PRIMARY KEY AUTOINCREMENT,
  #   userName NVARCHAR(20) NULL,
   #  email NVARCHAR(30) NOT NULL,
    # phone NVARCHAR(20),
     #age INTEGER)""")
    #НАстройка уникальности данных
#cursor.execute("""CREATE TABLE Table_5
 #    (id INTEGER PRIMARY KEY AUTOINCREMENT,
  #   userName NVARCHAR(20) NULL,
   #  email NVARCHAR(30) NOT NULL,
    # phone NVARCHAR(20) UNIQUE,
     #age INTEGER)""")
#Настройка значения по умолчанию
#cursor.execute("""CREATE TABLE Table_6
 #    (id INTEGER PRIMARY KEY AUTOINCREMENT,
  #   userName NVARCHAR(20) DEFAULT Taras777,
   #  email NVARCHAR(30) NOT NULL,
    # phone NVARCHAR(20) UNIQUE,
     #age INTEGER)""")

#  ДОюовление данных в таблицу
#cursor.execute("""INSERT INTO Account
#VALUES('Ivan1997', 'ivan1997@gmail.com', '+3800994354321', 33)""")
#cursor.execute("""INSERT INTO Table_2
#VALUES(1, 'ivan1997@gmail.com', '+3800994354321', '33',0)""")

#cursor.execute("""INSERT INTO Table_3
#VALUES(1,'', NULL, '+3800994354321', 33)""")

#add dannie
list_1 = ["dfsdf","sdf.sd","1323413"]
cursor.execute(f"""INSERT INTO Table_2
VALUES(4, ?, ?, ?,4)""", list_1)
#Подтверждение изменений
conn.commit()


#Закрыть подключение
conn.close()