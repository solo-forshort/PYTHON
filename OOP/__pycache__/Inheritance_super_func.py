class atuIST:
    def __init__(self, fname, lname, position):
        self.fname = fname
        self.lname = lname
        self.position = position

    def showStaff(self):
        print("Staff name is: ", self.fname, " ", self.lname)
        print("Position of Staff: ", self.position)

#child Class: staffIST
class staffIST(atuIST):
    def __init__(self, fname, lname, position, age, salary):
        super().__init__(fname, lname, position)
        self.age = age
        self.salary = salary

    def staffSal(self):
        print(self.fname," ", self.lname, "is", self.age, "years old and salary is: ",self.salary)

#creating object
staff = staffIST("Solomon", "Asare", "Lecturer", 24, 5000)
staff.showStaff()
staff.staffSal()

