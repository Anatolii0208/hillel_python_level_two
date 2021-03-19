#основные модули языка пайтон
from math import sqrt,factorial,cos,pow
from csv import *
def calculator(a):
    b = list(a.split())
    c = 0
    if b[1] == "+":
        c = int(b[0]) + int(b[2])
    elif b[1] == "-":
        c = int(b[0]) - int(b[2])
    elif b[1] == "*":
        c = int(b[0]) * int(b[2])
    elif b[1] == "//":
        c = int(b[0]) // int(b[2])
    elif b[1] == "pow":
        c = pow(int(b[0]),int(b[2]))
    elif b[1] == "sqrt":
        c = sqrt(int(b[0]))
    elif b[1] == "cos":
        c = cos(int(b[0]))
    else:
        c = factorial(int(b[0]))
    return c
a = int(input())
dict_calc = {}
for i in range(a):
    b = input()
    dict_calc[b] = calculator(b)
with open('path.csv', 'w') as csv_file:
    writer = writer(csv_file)
    for key, value in dict_calc.items():
       writer.writerow([key, value])
with open('path.csv','r') as csv_file:
    reader = reader(csv_file)
    dict_calc = dict(reader)
    list_end=(list(dict_calc.values())[0:5])
    list_end = [float(i) for i in list_end]
    print(round(sum(list_end)))