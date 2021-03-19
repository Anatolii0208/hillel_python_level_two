lol = 23 # int
std = "lkvghf" # str
strr = 0.0 #float

#print("Age: {} Name VAssya, {} , Real number = {}", (lol, std, strr))

print("Age: %d Name VAssya, %s , Real number = %f"%(lol, std, strr))

#Отключение перехода на новую строку
print("ROW_1: ", end="")
print("ROW_2: ")

"""Multi str 'comments'  """
''' tnty"rgfpkrepogoreg"reg rejg oprejgpore'''

lor = input("Введите число: ") #str
dss = int(input("Input number"))#int

print(lor, type(lor))
print(dss, type(dss))

"""
Math operator
 / * + -
 +=
 -=  4 -= 3 - >>> 4 =(4 - 3)  = 1 
 **  2 ** 3 = 8
 //  10 // 3 = 3
 %    10 % 2 = 0
 not      
"""

srt = "number of win"


#STRING SLISING
print(srt[4])
#srt[start_index :  finish_index]
print(srt[4:9])
#srt[start_index :  finish_index : step]
print(srt[::2])

#fun for STR
print(srt.upper())
print(srt.lower())

print(len(srt))#Длинна строки целім числом

srt = srt.replace("n", "Z") #Заменяет символы в копии строки
print(srt)

#srt = "number of win"
print(srt.rindex("ber"))

print("\n".join(['regfreg', "regreg", "RRfde"]))



