class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("woof!")

class Cat(Animal):
    def speak(self):
        print("meow!")

class Mouse(Animal):
    def speak(self):
        print("squeek!")

dog = Dog("scooby")
cat = Cat("garfield")
mouse = Mouse("mickey")
animal = Animal("animal")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()