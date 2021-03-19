import datetime
class Train:
    def __init__(self, n, num, d, m):
        #инкапсулированые переменные
        self.name = n
        self.number = num
        self.time = d*24+m
        #normal

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if len(n) in range(1,15):
            self.__name = n
        else:
            self.name = input("введите правильное название пункта назначения")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, n):
        if 0<n<52:
            self.__number = n
        else:
            self.number = int(input("введите реальный номер поезда"))

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, n):
        if n >= datetime.datetime.now().day*24+datetime.datetime.now().hour:
            self.__time = n
        else:
            self.time = int(input("введите правильный день отправления поезда с номером", self.__number))

    def trrain(self):
        print(f"Название пункта назначения: {self.__name}, день отправления: {self.__number} время отправления: {self.__time // 24} {self.__time % 24}")
