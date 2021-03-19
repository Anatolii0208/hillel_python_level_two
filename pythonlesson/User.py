class User:
    def __init__(self, n, s):
        #инкапсулированные
        self.name = n
        self.sirname = s

    def getFullName(self):
        print(f"Ваше имя:{self.__name} Ваша фамилия:{self.__sirname}")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,n):
        if len(n) in range(1,15):
            self.__name = n
        else:
            self.name = input("неправильный формат имени")

    @property
    def sirname(self):
        return self.__sirname

    @sirname.setter
    def sirname(self, n):
        if len(n) in range(1, 15):
            self.__sirname = n
        else:
            self.sirname = input("неправильный формат фамилии")