from sqlite3 import *
#Функции SQL // SRF - Single-row Function


con = connect("Chinook_Sqlite.sqlite")
cur = con.cursor()

   #LENGTH - длинна строчного обьекта (поля, записи, ячейки таблици в бд)
'''
cur.execute("""SELECT Name
                    FROM Artist
                        WHERE LENGTH(Name) < 6
""")
'''

#LOWER()
#UPPER()
#INSTR()
'''cur.execute("""SELECT Name
                    FROM Artist
                        WHERE INSTR(LOWER(Name), 'b') > 0
""")'''

#MOD()
'''
cur.execute("""SELECT *
                    FROM Track
                        WHERE MOD(Milliseconds, 10) = 0
""")
'''

#SUBSTR()
'''cur.execute("""SELECT SUBSTR(Name, 1, INSTR(Name, ' ') - 1 )
                    FROM Track
""")'''

#COUNT()
#IS
#NULL
# IS NOT
'''cur.execute("""SELECT COUNT(*)
                    FROM Track 
                    WHERE Composer IS NULL
""")
'''

#BETWEEN()
'''
cur.execute("""SELECT COUNT(*)
                    FROM Track 
                    WHERE Milliseconds  BETWEEN 1000 AND 100000
""")
'''

#CASE
'''cur.execute("""SELECT Name, Composer,
                        CASE
                                WHEN Milliseconds < 100000 THEN 'short song'
                                WHEN Milliseconds BETWEEN 100000 AND 250000 THEN 'medium song'
                                WHEN Milliseconds > 250000 THEN 'long song'
                                ELSE 'Unknown'
                        END
                              length_song  
                    FROM Track 

""")'''


#Agrigate
#GROUP BY
'''
cur.execute("""SELECT COUNT(*),
                        CASE
                                WHEN Milliseconds < 100000 THEN 'short song'
                                WHEN Milliseconds BETWEEN 100000 AND 250000 THEN 'medium song'
                                WHEN Milliseconds > 250000 THEN 'long song'
                                ELSE 'Unknown'
                        END
                              length_song  
                    FROM Track 
                    GROUP BY length_song

""")'''

'''
cur.execute("""SELECT Name, Composer,
                        CASE
                                WHEN Milliseconds < 100000 THEN 'short song'
                                WHEN Milliseconds BETWEEN 100000 AND 250000 THEN 'medium song'
                                WHEN Milliseconds > 250000 THEN 'long song'
                                ELSE 'Unknown'
                        END
                              length_song  
                    FROM Track 
                    WHERE  length_song = 'short song' AND Composer IS NOT NULL

""")'''
'''
cur.execute("""SELECT COUNT(*), Name, Composer
                    FROM Track 
                    WHERE Composer IS NOT NULL
                    GROUP BY Composer
""")
'''

#HAVING - оператор пост обработки данных после агрегации
'''
cur.execute("""SELECT COUNT(*), Name, Composer
                    FROM Track 
                    WHERE Composer IS NOT NULL
                    GROUP BY Composer
                    HAVING COUNT(*) >= 3
""")
'''


#1 Найти Из таблиц Customer те записи у которых FirstName менее 6и символов
'''cur.execute("""SELECT FirstName
                    FROM Customer 
                    WHERE LENGTH(FirstName) < 6

""")'''

#2 Подсчитать количество записей Из таблиц Customer у которых нет телефонного номера
'''cur.execute("""SELECT COUNT(*), FirstName
                    FROM Customer 
                    WHERE Phone IS NULL
""")'''

#3 сгрупировать всех клиентов по странам и подсчитать сколько клиентов из каждой страны

'''cur.execute("""SELECT COUNT(*), Country
                    FROM Customer
                    GROUP BY Country 
""")'''

#4 У скольких Customer все Postal_Code начинаются с буквы

'''
cur.execute("""SELECT PostalCode
                    FROM Customer 
                    WHERE PostalCode LIKE '_%'
                    
""")

for el in cur.fetchall():
    if el[0][0].isalpha():
        print(el)
'''

#5 Найти самый длинный email и вывести все записи у которых email такой же длинны

cur.execute("""SELECT Email, COUNT(*)
                    FROM Customer 
                    GROUP BY LENGTH(Email)

""")

lol = max( [ el[0] for el in cur.fetchall() ] )
print(lol)

#for el in cur.fetchall():
#    if el[0][0].isalpha():
#        print(el)

#6 Сколько Customer прилетело из Лондона, Парижа, Берлина

'''cur.execute("""SELECT COUNT(*), City
                    FROM Customer 
                    GROUP BY City
                    HAVING City = 'London' OR City = 'Paris' OR City = 'Berlin' 
""")'''




for el in cur.fetchall():
    print(el)
con.close()