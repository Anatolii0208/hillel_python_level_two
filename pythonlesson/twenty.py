from sqlite3 import *
import os
import sys

def writeImage(address):
    try:
        im_1 = None
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

'''cur.execute("""
    CREATE TABLE IF NOT EXISTS Artist()
""")'''

# мета инфо
#cur.execute("""PRAGMA table_info(Track)""")

#SELECT
'''cur.execute("""SELECT name, rootpage, sql, tbl_name, type 
                FROM sqlite_master
""")

for el in cur.fetchall():
    print(el)
'''

'''try:
    print(20 / 0)
    sys.exit(1)
except IOError as e:
    print(e.args[0])
'''

cur.execute("""CREATE TABLE IF NOT EXISTS Storage_1(
                ImageId INTEGER NOT NULL UNIQUE,
                ImageData BLOB NOT NULL
)""")
con.commit()

list_image = os.listdir("Images")
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
                                VALUES(?,?)""",(list_image.index(address), binary_data))
            con.commit()
        else:
            print("Image does not exist")





cur.close()