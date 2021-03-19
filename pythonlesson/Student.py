from User import *
class Student(User):
    def __init__(self,n, a, y):
        User.__init__(self, n, a)
        self.year = y

    def getCourse(self, now_year):
        #now_year = int(input())
        print( now_year - self.year)

