from sqlite3 import *

con = connect("Chinook_Sqlite.sqlite")
cur = con.cursor()

cur.execute("""SELECT *
                FROM Customer
                WHERE Company IS NOT NULL
                GROUP BY LENGTH(Company)
""")
list_d  = cur.fetchall()
max_lenth = 0
for el in list_d:
    if len(el[3]) > max_lenth:
        max_lenth = len(el[3])
list_2 = [ el for el in list_d if len(el[3]) == max_lenth]
print(list_2)

cur.execute("""SELECT COUNT(*)
                FROM Customer
                WHERE Company IS NULL AND FAX IS NULL
""")
print(cur.fetchall())

cur.execute("""SELECT COUNT(*),
            CASE 
                WHEN Country='Brazil' OR Country='Chile' THEN 'south america'
                WHEN Country='Canada' OR Country='USA'  THEN 'north america'
                WHEN Country='India'  THEN 'africa'
                ELSE 'evrasia'
            END
                length_song
                FROM Customer
                GROUP BY length_song
""")
for el in cur.fetchall():
    print(el)
#WHEN Country=Germany OR Country=Norway OR Country=Czech Republic OR Country=Belgium THEN '
#WHEN INSTR(Country,'Brazil')=1 OR INSTR(Country,'Chile')=1 THEN 'south america'
con.close()