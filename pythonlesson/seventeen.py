from sqlite3 import *

#DDL - язык создания / определения данных
    #CREAT - запрос на создание таблицц
    #DROP - на удаление таблицц
    # TRUNCATE - очищает все данные таблицц, но сама таблица остается
    #ALTER редактироввать / изменять уже готовых таблиц
#DML - язык манипуляции данными
    #SELECT - извлучения данных из бд
    #UPDATE - обновление суш данных
    #INSERT - добавление данных / вставка в бд
    #DELETE - удаление данных
#DSL - язык управления доступа к данным
    #GRANT - предоставления права доступа к данным
    #REVOKE - забирает права на доступ к данным

con = connect("Chinook_Sqlite.sqlite")
cur = con.cursor()

#извлечение всех данных из бд
#cur.execute("""SELECT Name
#                    FROM Artist
#                       LIMIT 10""")

#Запрос на выборку данных
#cur.execute("""SELECT *
 #                   FROM Artist
  #                  ORDER BY ?
   #                     LIMIT ?""",(input(),input(),))

#cur.execute("""SELECT *
 #                   FROM Artist
  #                  WHERE Name LIKE 'A%'
   #                     LIMIT 5""")

#cur.execute("""SELECT Address,City,Email
 #                   FROM Customer
  #                 WHERE Country = "USA"
   #                      """)
#cur.execute("""SELECT *
 #                   FROM Employee
  #                  WHERE FirstName = "Jane"
   #                     """)
#cur.execute("""SELECT FirstName, LastName
 #                   FROM Customer
  #                  WHERE  1 < SupportRepId < 4
   #                     """)
#cur.execute("""SELECT FirstName, LastName
 #                   FROM Customer
  #                  WHERE FirstName LIKE '%a'
   #                     """)
#cur.execute("""SELECT FirstName, LastName
 #                   FROM Customer
  #                  WHERE Company is NOT NULL
   #                     """)
cur.execute("""SELECT LastName, FirstName
                    FROM Customer
                    WHERE FirstName LIKE '%n%n%' OR '%t%t%'
                        """)

#cur.execute("""SELECT FirstName, LastName
 #                   FROM Customer
  #                  WHERE LENGTH(FirstName) > 4
   #                     """)
#Вывод результата в коде
list_d = cur.fetchall()
print(list_d)

con.close()