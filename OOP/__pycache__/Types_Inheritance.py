class Staff:
    def __init__(self, name):
        self.name = name

#Single Inheritance
# class IST_staff(Staff): #Employee inherits from staff
    # def __init__(self, name, salary):
    #     super().__init__(name)
    #     self.salary = salary

#Multiple Inheritance
class Position:
    def __init__(self, salary):
        self.salary = salary
class StaffPosition(Staff, Position): #Inherits from both staff and position
    def __init__(self, name, salary):
        Staff.__init__(self, name)
        Position.__init__(self, salary)

#Multiple Inheritance
class Boss(StaffPosition):
    def __init__(self, name, salary, department):
        StaffPosition.__init__(self, name, salary)
        self.department = department

        #Hierarchical
        #Hybrid