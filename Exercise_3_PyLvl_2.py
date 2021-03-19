import random
'''
def function(a, lol, b):
    print("Privet ya func")

    if a > lol and a > b:
        print(f"a = {a}")
        return a
    elif lol > b and lol > a:
        print(f"lol = {lol}")
        return lol
    elif b > a and b > lol:
        print(f"b = {b}")
        return b
    
    #Функция нам чтото вернет если ни одно из условий не сработает
    return 0


fr = 100
d = 100
lol = 100

peremennaya = function(fr, d, lol)
print(f"RETURN {peremennaya + 152}")
print("Eto ne func :(")
'''

'''
def colGlaNe(st):
    glas = 0
    neGla = 0
    neBukvi = 0
    for el in st:
        if el.lower() in "aeouiаеуоиёюы":
            glas+=1
        elif el.lower() in "qwrtypsdfghjklzxcvbnmйцкнгшщзхфвпрлджчсмтьбъ":
            neGla += 1
        else:
            neBukvi += 1
    print(f"Glas = {glas}\nNeGlas = {neGla}\nNeBukvi = {neBukvi}")

stri = input("Введите строку")

colGlaNe(stri)
'''

'''
def cryptingNum(num):
    "380992024024"
    rez = []
    result = ""
    #Сдвиг по числам
    for el in num:
        if int(el) + 3 > 9:
            result += str( (int(el) + 3) % 10 )
        else:
            result += str(int(el) + 3)
    rez.append(int(result))
    result = ""
    #Сдвиг по строке String RIFT
    for i in range(len(num)):
        if i + 3 > len(num) - 1:
            index = (i + 3) - (len(num))
            result += num[index]
        else:
            result += num[i + 3]
    rez.append(result)
    return rez

#index = 0 1 2 3 4 5 6 7 8 9  10 11
#len   = 1 2 3 4 5 6 7 8 9 10 11 12

num = input("Input number phone")

#проверка возвращаемого типа
if type(cryptingNum(num)) == type(str()):
    print(type(cryptingNum(num)))

#num = cryptingNum(num)
print(f"Num is crypting = {cryptingNum(num)}")
'''

#Логические функции
'''def poly(st):
    st.replace(" ", "")
    return st == st[::-1]

#st = input("Input symbol: ").replace(" ", "")
st = input("Input symbol: ")
print(f"String = {st} is a poly: {poly(st)}")
'''

'''
def poly(st):
    return st == st[::-1]

#st = input("Input symbol: ").replace(" ", "")
st = int(input("Input symbol: "))
print(f"String = {st} is a poly: {poly(str(st))}")
'''

def bolshe(a, b):
    return len(a) > len(b)

def countGlas(st):
    glas = 0
    neGlas = 0

    for el in st:
        if el.lower() in "aeouiаеуоиёюы":
            glas += 1
        elif el.lower() in "qwrtypsdfghjklzxcvbnmйцкнгшщзхфвпрлджчсмтьбъ":
            neGlas += 1

    return glas > neGlas

str_1 = "aaa"
str_2 = "bbdgfwf"


#if not bolshe(str_1, str_2):  # if bolshe(str_1, str_2) == False:
if bolshe(str_1, str_2): #if bolshe(str_1, str_2) == True:
    print(f"{str_1} > {str_2}")
else:
    print(f"{str_1} <= {str_2}")