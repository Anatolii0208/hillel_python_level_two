from datetime import *
#13
#13_1
"""
class User:
    def __init__(self, n, s):
        #/Инкапсулированные
        self.name = n
        self.surname = n

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, n):
        if len(n) in range(1, 50):
            self.__name = n
        else:
            self.__name = "Taras"

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, n):
        if len(n) in range(1, 50):
            self.__surname = n
        else:
            self.__surname = "Otamanov"

    def getInfo(self):
        #print(f"name: {self.__name}, surname = {self.__surname}")
        return f"name: {self.name}, surname = {self.surname}"

class Student(User):
    def __init__(self, n, s, yr):
        User.__init__(self,n, s)
        self.year = yr

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if y in range(1950, 2021):
            self.__year = y
        else:
            self.__year = 1950

    def getCourse(self, y):
        if  abs(self.year - y) > 13:
            print("Учеба закончена давно((( Уже не студент")
        else:
            print(f"course = {abs(self.year - y)} ")

stud_1 = Student("Ludmila", "Zorina", 2017)
stud_2 = Student("Halif", "Butan", 2100)
stud_3 = Student("Abdula", "Bekmambetov", 2000)

currentY = int(datetime.now().year)
print(currentY)

print(stud_1.getInfo())
stud_1.getCourse(currentY)

print(stud_2.getInfo())
stud_2.getCourse(currentY)

print(stud_3.getInfo())
stud_3.getCourse(currentY)
"""
#13_2
"""
class Vine:
    def __init__(self, v):
        self.vine = v

    @property
    def vine(self):
        return self.__vine

    @vine.setter
    def vine(self, v):
        self.__vine = {key : elem for key, elem in v.items() if not key == None and not key == "" and elem in range(1600, 2021) }

    def exeptions(self, nameV):
        return {key : self.vine[key] for key in self.vine.keys() - {nameV} }

    def countBotle(self, year):
        return len({key : elem for key, elem in self.vine.items()  if elem > year})

    def longestName(self):
        return { el: self.vine[el] for el in self.vine.keys() if len(el) == max( len(key) for key in self.vine.keys() ) }

    def sorYear(self):
        def next(el):
            return el[1]
        return {key: el for key, el in sorted(self.vine.items(), key=next ) }


vines = {"19Crimes" : 2017, "Abrau Wite": 2014, "Alamos Chardonnay":2013, "Alushta Dry Massandra Collection" : 1988, "Aretino Tipici Chianti Classico" : 2010}
print(vines)

vin = Vine(vines)
print(vin.exeptions("Alamos Chardonnay"))
print(vin.countBotle(2013))
print(vin.longestName())
print(vin.sorYear())
"""

#14
class Train:
    def __init__(self, n, num, dep):
        self.targetStation = n
        self.number = num
        self.depTime = dep

    @property
    def targetStation(self):
        return self.__targetStation

    @targetStation.setter
    def targetStation(self, n):
        if not n in ("", None):
            self.__targetStation = n
        else:
            self.__targetStation = "Kharkiv"

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, n):
        if not n in (0, None):
            self.__number = n
        else:
            self.__number = 1

    @property
    def depTime(self):
        return self.__depTime

    @depTime.setter
    def depTime(self, dataTIME):
        if not int(datetime.now().hour) > dataTIME[0] and not int(datetime.now().day) > dataTIME[1] :
            self.__depTime = dataTIME
        else:
            self.__depTime = [int(datetime.now().hour), int(datetime.now().day)]


listTrain = [
    Train("Budapesht", 23, [19, 20]),
    Train("Lviv", 324, [22, 21]),
    Train("Budapesht", 5, [14, 20]),
    Train("Smela", 78, [19, 26]),
    Train("Varna", 99, [23, 19]),
    Train("Kiev", 13, [22, 30]),

]

#14_1
"""
def next(objTrain):
    return objTrain.number

listSort = sorted(listTrain,key=next)
for el in listSort:
    print(el.targetStation, el.depTime, el.number)
"""

#14_2
def next(objTrain):
    return objTrain.targetStation


for i in range(len(listTrain)):
    for j in range(len(listTrain) - 1 - i):

        if next(listTrain[j]) > next(listTrain[j + 1]):
            listTrain[j], listTrain[j + 1] =  listTrain[j + 1], listTrain[j]

        elif next(listTrain[j]) == next(listTrain[j + 1]):
            if listTrain[j].depTime[0] > listTrain[j + 1].depTime[0]:
                listTrain[j], listTrain[j + 1] = listTrain[j + 1], listTrain[j]

#listSort = sorted(listTrain,key=next)
for el in listTrain:
    print(el.targetStation, el.depTime, el.number)

