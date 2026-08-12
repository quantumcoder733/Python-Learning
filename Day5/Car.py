class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def diplayInfo(self):
        print("Brand", self.brand)
        print("Model", self.model)
        print("Year", self.year)
        

c1 = Car("mustang","G100",1944)
c2 = Car("Ferari","f50",1950)

c1.diplayInfo()
c2.diplayInfo()


#inheritance
class Vehicle:
    def __init__(self,brand):
        self.brand = brand


    def start(self):
        print("Vehicle Started !!")


class Car2(Vehicle):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model = model
    
    def display(self):
        print("Brand :",self.brand)
        print("Model :",self.model)

c3 = Car2("Toyota","supra")
c3.start()
c3.display()

    
        