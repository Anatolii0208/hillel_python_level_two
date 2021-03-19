from sqlite3 import *

#DDL - язык создания / определения данных
    #CREATE - запрос на создание таблиц
    #DROP - на удаление таблиц
    #TRUNCATE - очищает все данные таблици, но сама таблица остается
    #ALTER - редактирование / изменение уже готовых таблиц
#DML - язык манипуляцией данными
    #SELECT - извлечение данных из бд
    #UPDATE - обновление сущ данных
    #INSERT - добавление данных в бд или вставка
    #DLETE - удаление данных
#DCL - управление доступом к данным
    #GRANT - предоставление права доступа к данным
    #REVOKE - отзывает права на доступ к данным


#LIMIT - ограничение выборки по количеству
#ORDER BY - сортировка данных запроса
#WHERE - условный оператор
#LIKE - указывает на шаблон поиска

con = connect("Chinook_Sqlite.sqlite")
cur = con.cursor()

#Извлечение всех данных из бд
#cur.execute("""SELECT Name
#                    FROM Artist
#                        LIMIT 10""")


#Вывод результата в коде

#Запрос на выборку данных с ограничением по количество и сортировкой по имени
#cur.execute("""SELECT *
#                    FROM Artist
#                    ORDER BY Name
#                        LIMIT 10""")
#Управление запросами из кода
#cur.execute("""SELECT *
#                    FROM Artist
#                    ORDER BY ?
#                        LIMIT ?""", (
#                                        input("Введите имя поля для сортировки"),
#                                        input("Введите количество записей"),
#                                    )
#            )


#cur.execute("""SELECT *
#                    FROM Artist
#                    WHERE (Name LIKE '%ac%')  OR ( ArtistId = 13)
#                    LIMIT 10""")


#Вывести все данные о сотруднике Jane из таблици Employee
"""SELECT *
        FROM Employee
        WHERE FirstName = 'Jane'
        """

#Вывести Адрес, Город, Email, из таблици Customer тех сотрудников у которых Страна USA
"""SELECT Address, City, Email
        FROM Customer
        WHERE Country = 'USA'
"""

#Таблица Customer. Получить список всех сотрудников
# у которых SupportRepId  менее 4 но более 1
"""SELECT FirstName, LastName
        FROM Customer
        WHERE (SupportRepId > 1)  AND (SupportRepId < 4) 
"""

#Таблица Customer.
# Получить список всех покупателей у которых последняя буква в имени равна 'a'

"""SELECT FirstName, LastName
        FROM Customer
        WHERE FirstName LIKE '%a'
"""

#Таблица Customer.
# Получить список всех сотрудников из у которых поле Company не пустое
"""SELECT FirstName, LastName
        FROM Customer
        WHERE Company IS NOT NULL
"""
#Таблица Customer. Получить список всех сотрудников у которых
# в имени содержатся минимум 2 буквы 'n' или 2 буквы t
cur.execute("""SELECT FirstName, LastName
        FROM Customer
        WHERE FirstName LIKE '%n%n%' OR '%t%t%'
""")
#Таблица Customer.
# Получить список всех сотрудников у которых длина имени больше 4 букв

list_d = cur.fetchall()
print( list_d)