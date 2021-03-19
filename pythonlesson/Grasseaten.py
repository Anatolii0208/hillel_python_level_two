from Alltypes import *
class Grasseaten(Alltypes):
    def __init__(self,k_f,t_f,indificate,n_a):
        Alltypes.__init__(self,k_f,t_f)
        self.indificate = indificate
        self.name_animal = n_a