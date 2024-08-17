#polymorphism:

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("sail!")

class Plane(Vehicle):
    def move(self):
        print("fly!")

car1 = Car("ford", "mustang")
boat1 = Boat("ibiza", "touring 20") 
plane1 = Plane("boeing", "747") 

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()