#Encaptulation

class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self,marks):
        if marks>=0 and marks<=100:
            self.__marks = marks
        else:
            print("invalid Marks")

    def get_marks(self):
        print("Marks : ",self.__marks)

s = Student()

s.set_marks(95)
s.get_marks()

s.set_marks(150)
s.get_marks()
        
