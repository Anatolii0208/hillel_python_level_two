from sqlite3 import *
import os
import sys

def writeImage(address):
    im_1 = None
    try:
        with open(address, "rb") as image:
            im_1 = image.read()
    except Exception as e:
        print(e)
    finally:
        if im_1:
            return im_1
        else:
            return None

con = connect("ImageStorehw.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Storage_1(
    ImageId INTEGER NOT NULL UNIQUE,
    ImageGanr TEXT,
    ImageData BLOB NOT NULL
)""")
con.commit()

list_image = os.listdir("Images")
list_ganr = []
for i in range(len(list_image)):
    if i % 4 == 0:
        list_ganr.append(None)
    else:
        list_ganr.append("hillel" + str(i % 4))

for address in list_image:
    image_data = writeImage("Images/" + address)
    binary_data = None
    try:
        binary_data = Binary(image_data)
    except Exception as e:
        print(e)
    finally:
        if binary_data:
            cur.execute("""INSERT INTO Storage_1
                                VALUES(?,?,?)""",(list_image.index(address), list_ganr[list_image.index(address)], binary_data))
            con.commit()
        else:
            print("Image does not exist")

if os.path.exists("Image") == False:
    os.mkdir("Image")

#Вывести по одной картинке (то есть сохранить в папку результат) из 3х жанров (желательно одним запросом, или скрипт запросом)
cur.execute("""SELECT *
                    FROM Storage_1
                    ORDER BY ImageGanr
                    """)

list_d = cur.fetchall()
ganr = ''
for i in list_d:
    if i[1] != ganr and i[1] != None:
        with open("Image/image"+str(list_d.index(i))+"1.jpg","wb") as image:
            image.write(i[2])
        ganr = i[1]

#Вывести каждую 2ю картинку (то есть сохранить в папку результат) одного из жанров

cur.execute("""SELECT *
                    FROM Storage_1
                    ORDER BY ImageGanr
                    """)

list_d = cur.fetchall()
ganr = list_d[0][1]
i = 0
while list_d[i][1] == ganr:
    if i % 2 == 1:
        with open("Image/image"+str(i)+"2.jpg","wb") as image:
            image.write(list_d[i][2])
    i+=1

#Вывести все картинки без жанра (то есть сохранить в папку результат)
cur.execute("""SELECT *
                    FROM Storage_1
                    WHERE ImageGanr IS NULL
                    """)

list_d = cur.fetchall()
for el in list_d:
    with open("Image/image" + str(list_d.index(el)) + "3.jpg", "wb") as image:
        image.write(el[2])

#Всем картинкам без жанра присвоить жанр "Unknown", результат вівести на єкран в виде запроса
cur.execute("""UPDATE Storage_1
                SET ImageGanr = 'Unknown' 
                WHERE ImageGanr IS NULL
                """)
con.commit()

con.close()