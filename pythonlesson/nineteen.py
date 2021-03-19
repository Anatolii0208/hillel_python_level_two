from sqlite3 import *
#функции SQL // SRF - Single-row Function
    #LENGTH - длинна строчного объекта (поля, записи, ячейки, таблици в бд)

con = connect("Chinook_Sqlite.sqlite")
cur = con.cursor()

'''cur.execute("""SELECT Name 
                FROM Artist
                    WHERE LENGTH(Name) < 6 
""")'''

#LOWER()
#UPPER()
'''cur.execute("""SELECT LOWER(Name) 
                FROM Artist
                    WHERE LENGTH(Name) < 6 
""")'''

#INSTR()
'''cur.execute("""SELECT Name 
                FROM Artist
                    WHERE INSTR(LOWER(Name),'b') > 1 
""")'''

#MOD()
'''cur.execute("""SELECT Name 
                FROM Track
                    WHERE MOD(Milliseconds, 10) > 1 
""")'''

#SUBSTR
'''cur.execute("""SELECT SUBSTR(Name, Composer) 
                FROM Track
""")'''

#COUNT
#IS
#NULL
'''cur.execute("""SELECT COUNT(*) 
                FROM Track
                    WHERE Composer IS NULL
""")'''

#BETWEEN // in python range
'''cur.execute("""SELECT COUNT(*) 
                FROM Track
                    WHERE Milliseconds BETWEEN 1000 AND 100000
""")'''

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

#GROUP BY
'''cur.execute("""SELECT Count(*),
            CASE 
                WHEN Milliseconds < 100000 THEN 'short song'
                WHEN Milliseconds BETWEEN 100000 AND 250000 THEN 'medium song'
                WHEN Milliseconds > 250000 THEN 'long song'
                ELSE 'Unknown'
            END
                length_song
                FROM Track
                GROUP BY length_song
""")
'''

'''cur.execute("""SELECT Name,
            CASE 
                WHEN Milliseconds < 100000 THEN 'short song'
                WHEN Milliseconds BETWEEN 100000 AND 250000 THEN 'medium song'
                WHEN Milliseconds > 250000 THEN 'long song'
                ELSE 'Unknown'
            END
                length_song
                FROM Track
                WHERE length_song = 'short song'
""")'''

'''cur.execute("""SELECT COUNT(*),Name
                FROM Track
                WHERE Composer IS NOT NULL
                GROUP BY Composer
""")'''

#HAVING
'''cur.execute("""SELECT COUNT(*),Name
                FROM Track
                WHERE Composer IS NOT NULL
                GROUP BY Composer
                HAVING COUNT(*) > 3
""")'''

#Tasks
'''cur.execute("""SELECT FirstName
                FROM Customer
                WHERE LENGTH(FirstName) < 6
""")'''

'''cur.execute("""SELECT FirstName
                FROM Customer
                WHERE Phone IS NULL
""")'''

'''cur.execute("""SELECT COUNT(*),Country
                FROM Customer
                GROUP BY Country
""")'''

'''cur.execute("""SELECT COUNT(*)
                FROM Customer
                WHERE PostalCode LIKE '_%'
""")'''

cur.execute("""SELECT Email, FirstName
                FROM Customer
                ORDER BY LENGTH(Email)
""")
for el in cur.fetchall():
    print(el)

con.close()