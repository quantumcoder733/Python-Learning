#inheritance

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi I am {self.name} and i am {self.age} years Old")

class Employee(Person):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary = salary

    def work(self):
        print("I am Working")

class Manager(Employee):
    def __init__(self, name, age, salary,department):
        super().__init__(name, age, salary)
        self.department = department

    def manage(self):
        print("Manages AI Team")

    def display(self):
        print(f"My name is {self.name} and i am {self.age} years old and my salary is {self.salary} and my department is {self.department}")


m = Manager("Musaddiq", 19, 50000, "AI Team")
m.introduce()
m.work()
m.manage()
m.display()