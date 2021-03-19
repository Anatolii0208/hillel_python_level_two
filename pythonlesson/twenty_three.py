from random import randint
from datetime import *
import time

def end_buble(buble):
    def wrap(b):
        print(f"{buble(b)}\n array is sorted by buble sort")
    return wrap



def end_stupid(stupid):
    def wrap(data):
        print(f"""{stupid(data)}\narray is sorted by stupid sort""")
    return wrap



def timer_fun(func):
    """Декоратор для вычесления времени работы функции"""
    def wrap(a):
        print(a)
        start = datetime.now()
        func(a)
        finish = datetime.now()

        time_d = (finish - start).total_seconds() * 1000

        print("Time running", time_d)

    return wrap

@timer_fun
@end_buble
def buble(a):
    N = len(a)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

@timer_fun
@end_stupid
def stupid(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] > data[i]:
            data[i - 1], data[i] = data[i], data[i - 1]
            i = 1
        else:
            i += 1
    return data

five_hundred = [randint(1,1000) for i in range(500)]
thousend = [randint(1,1000) for i in range(1000)]
hundred = [randint(1,1000) for i in range(100)]

buble(hundred)
buble(five_hundred)
buble(thousend)

five_hundred = [randint(1,1000) for i in range(500)]
thousend = [randint(1,1000) for i in range(1000)]
hundred = [randint(1,1000) for i in range(100)]

stupid(hundred)
stupid(five_hundred)
stupid(thousend)