class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result
#Create object 
calc = Calculator()
# print(calc.multiply()) #using default argument
# print(calc.multiply(5, 2)) #using multiple arguments 
    
## Runtime - Method Overloading
class Animal:
    def sound(self):
        return "Some generic sound"
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat(Animal):
    def sound(self):
        return "Meow"

#Polymorphism in Action
# animals = [Dog(), Cat(), Animal()]
# for animal in animals:
#     print(animal.sound())
# Checking animal types
# print(type(animals))
# print(type(animals[0]))  # Output: <class '__main__.Dog'>

#Polymorphism in built-in functions
#Example 
# print(len("Hello"))
# print(len([1, 2, 3]))
# print(len(("apple", "banana")))
# print(max(1, 2, 3))
# print(max("a", "b", "c"))
# print(min(1, 2, 3))

#Polymorphism in classes/functions
# Sample 1
class Pen:
    def use(self):
        return "Writing with a pen"
class Eraser:
    def use(self):
        return "Erasing with an eraser"
def perform_task(tool):
    print(tool.use())
# perform_task(Pen())  # Output: Writing with a pen
# perform_task(Eraser())  # Output: Erasing with an eraser

#sample 2
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Driving the car")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sailing the boat")

class Airplane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Flying the airplane")

car1 = Car("Toyota", "Camry")
boat1 = Boat("Yamaha", "242X")
airplane1 = Airplane("Boeing", "747")

for vehicle in (car1, boat1, airplane1):
    vehicle.move()  # Output: Driving the car, Sailing the boat, Flying the airplane
    