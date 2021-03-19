class Vine:
    def __init__(self,dv):
        #открытая переменная
        self.dict_vine = dv



    def sort_vine(self,):
        def next(item):
            return item[1]
        print({key: val for key, val in sorted(self.dict_vine.items(), key=next)})

    def with_out(self, name_vine):
        print([i for i in list(self.dict_vine.keys()) if i != name_vine])

    def kol_but(self,n):
        print(len( list(1 for i in list(self.dict_vine.values()) if i < n)))

    def the_longest_word(self):
        word = ''
        max_len = 0
        for i in list(self.dict_vine.keys()):
            if len(i) > max_len:
                word = i
                max_len = len(i)
        print(word)