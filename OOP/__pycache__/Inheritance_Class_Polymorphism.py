class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Moving the vehicle")
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sailing the boat")

class Airplane(Vehicle):
    def move(self):
        print("Flying the airplane")
car1 = Car("Toyota", "Camry")
boat1 = Boat("Yamaha", "242X")
airplane1 = Airplane("Boeing", "747")
for vehicle in (car1, boat1, airplane1):
    vehicle.move()
    print(vehicle.model)
    print(vehicle.brand)


#Polymorphism in Operators
#Example
print(5 + 3) #Integer addition
print("Hello " + "World") #String concatenation
print([1, 2] + [3, 4]) #List concatenation
