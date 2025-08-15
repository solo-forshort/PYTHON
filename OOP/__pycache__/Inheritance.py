class CyberStudent:
    def __init__ (self, fname, index):
        self.fname = fname
        self.index = index

#To check if this person is a student
    def display(self):
        print("Name:", self.fname)
        print("Index:", self.index)

###creating subclass/child class
# class CyberL100(CyberStudent):
#    pass #child inherits all properties from parent
    # def __init__(self, fname, index): #Adding __init__() function

# class CyberL200(CyberStudent):
#     def show(self):
#         print("I am a student in BTech Cyber L200")

class CyberClass(CyberStudent):
    def __init__(self, fname, index, age):
        CyberStudent.__init__(self, fname, index)
        self.student_age = age




### create a student oject
# student = CyberL100("Asare", "01242851b" )
# student.display()
# student2 = CyberL200("Kwame", "01242852b")
#calling Parent class
# student2.display()
# student2.show()  #calling child class method
student3 = CyberClass("Akosua", "0158b", 2)
student3.display()