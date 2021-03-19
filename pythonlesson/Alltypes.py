class Alltypes:
    type = ""
    indificate = 0
    name_animal = ""
    def __init__(self, k_f, t_f):
        #инкапсулированые
        self.kg_food = k_f
        self.type_food = t_f

    @property
    def kg_food(self):
        return self.__kg_food

    @kg_food.setter
    def kg_food(self, n):
        if 0 < n < 100:
            self.__kg_food = n
        else:
            self.__kg_food = 25


    @property
    def type_food(self):
        return self.__type_food

    @type_food.setter
    def type_food(self, n):
        if len(n) in range(1,11):
            self.__type_food = n
        else:
            self.__type_food = "grass"

    def all_about(self):
        print(f"type food:{self.__type_food} kg food:{self.__kg_food}")