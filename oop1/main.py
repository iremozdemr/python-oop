from car import Car

car1 = Car("mustang",2022,"blue")
car2 = Car("corvette",2023,"red")
car3 = Car("charger",2024,"green")
#obje oluşturma

print(car1)
#__str__ methodu yoksa adresi yazar
#__str__ methodu varsa objeyi yazar
print(car1.__dict__)
#dictionary halinde yazar
print(car1.model)
print(car1.year)
print(car1.color)

car1.drive()
car1.stop()
car1.describe()

print(car1.wheels)
print(car2.wheels)
print(car3.wheels)
print(Car.wheels)

print(car1.num_of_cars)
print(car2.num_of_cars)
print(car3.num_of_cars)
print(Car.num_of_cars)

del car1.color
#objenin değişkenini silme
del car1
#objeyi silme