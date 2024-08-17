class Person:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        
class Student(Person):
    def __init__(self,graduation_year):
        self.graduation_year = graduation_year 
#child class'a __init__ methodu eklenirse
#parent class'ın __init__ methodu bu class'ta geçersiz olur

class Teacher(Person):
    def __init__(self,name,lastname):
        Person.__init__(self,name,lastname)

class Doctor(Person):
    def __init__(self,name,lastname):
        super().__init__(name,lastname)

class Engineer(Person):
    def __init__(self,age,name,lastname):
        super().__init__(name,lastname)
        self.age = age

person = Person("name1","lastname1")
student = Student(2022)
teacher = Teacher("name2","lastname2")
doctor = Doctor("name3","lastname3")
engineer = Engineer(23,"name4","lastname4")

print(person.name, person.lastname)
print(student.graduation_year)
print(teacher.name, teacher.lastname)
print(doctor.name, doctor.lastname)
print(engineer.name, engineer.lastname, engineer.age)