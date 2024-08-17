from oop1.car import Car

car1 = Car("mustang",2022,"blue")
car2 = Car("corvette",2023,"red")
car3 = Car("charger",2024,"green")
#obje oluşturma

print(car1)
#adresi yazar

print(car1.__dict__)
#dictionary halinde yazar

print(car1.model)
print(car1.year)
print(car1.color)