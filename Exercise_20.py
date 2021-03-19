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

con = connect("ImageStore.db")
cur = con.cursor()

# cur.execute("""
# CREATE TABLE IF NOT EXISTS Artist (
#             idArtist INTEGER NOT NULL
#     )
# """)

#Мета инфо
#PRAGMA запрос
#cur.execute("""PRAGMA table_info(Artist)""")

# SELECT
# cur.execute("""SELECT name, rootpage, sql, tbl_name, type
#                 FROM sqlite_master
#                 WHERE type = 'table'
#                 """)
#
# for el in cur.fetchall():
#     print(el)

#ИСКЛЮЧЕНИЯ

# try: #Блок кода где возможно возникновение ошибки
#     num_1 = int(input())
#     num_2 = int(input())
#
#     if num_2 == 0:
#         raise Exception("Second numb not equal 0")
#
#     print(f"division = {num_1 / num_2}")
#
# except ZeroDivisionError:#обработка ошибок связаных только с делением на 0
#     print("На 0 делить незя")
#     sys.exit(1)
#
# except Exception as e:#обработка любых ошибок которые могут возникнуть try
#     print(e.args[0])
#
# else:#ВЫПОЛНЯЕТСЯ ТОЛЬКО ЕСЛИ НЕБЫЛО ОШИБКИ
#     print("ELSE")
#
# finally:#Блок необязателен, выполняется всегда после try / except ВЫПОЛЯНЕТСЯ ВСЕГДА вне зависимости от ошибок
#     print("FINALLY")

cur.execute("""CREATE TABLE IF NOT EXISTS Storage_1(
    ImageId INTEGER NOT NULL UNIQUE,
    ImageData BLOB NOT NULL
)""")

con.commit()

list_image = ["Imag/" + el for el in os.listdir("Image")]

for address in list_image:
    image_data = writeImage(address)
    binary_data = None
    try:
        binary_data = Binary(image_data)
    except Exception as e:
        print(e)
    finally:
        if binary_data:
            cur.execute("""INSERT INTO Storage_1
                                VALUES(?, ?)""", (list_image.index(address), binary_data))
            con.commit()
        else:
            print("Картинка не переобразована в бинарный формат")


con.close()