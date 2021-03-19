class MobPhone:
    def __init__(self,b,s_h,s_w,p):
        self.brand = b
        self.size_h = s_h
        self.size_w = s_w
        self.price = p


    def __del__(self):
        print(f" Бренд:{self.brand}, высота:{self.__size_h} ширина:{self.__size_w} цена:{self.price} \n ДАННЫЕ УДАЛЕНЫ")


    def getData(self):
        print(f" Бренд:{self.brand}, высота:{self.__size_h} ширина:{self.__size_w} цена:{self.price}")


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, n):
        if n > 0:
            self.__price = n
        else:
            print("error")
            self.name = int(input())

    @property
    def size_h(self):
        return self.__size_h

    @size_h.setter
    def size_h(self, n):
        if n <= 3200 and n >= 480:
            self.__size_h = n
        else:
            print("error of hieght")
            self.size_h = int(input())

    @property
    def size_w(self):
        return self.__size_w

    @size_w.setter
    def size_w(self, n):
        if n <= 3200 and n >=384:
            self.__size_w = n
        else:
            print("error of weidth")
            self.size_w = int(input())