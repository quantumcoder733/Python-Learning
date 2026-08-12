#Abstraction

class Shape:
    def area(self):
        pass

class Traingle(Shape):
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
        
    def area(self):
        return 1/2*length*breath

class Rectangle(Shape):
    def __init__(self,length,breath):
            self.length = length
            self.breath = breath

    def area(self):
        return length*breath 

class Circle(Shape):
    def __init__(self,radius):
            self.radius = radius
            
    def area(self):
        return 3.14*radius*radius

shapes = [Rectangle(4,5), Circle(3),Traingle(4,5)]

for s in shapes:
    print(s.area())
