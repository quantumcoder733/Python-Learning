#Method Overriding 
class Employee:
    def works(self):
        pass

class Developer(Employee):
    def works(self):
        print("Developer Writes Code")

class Designer(Employee):
    def works(self):
        print("Designer creates UI")

class Manager(Employee):
    def works(self):
        print("Manager Manages Team")

employees = [Developer(),Designer(),Manager()]

for employee in employees:
    employee.works()