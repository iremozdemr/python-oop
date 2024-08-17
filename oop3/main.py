class Person:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("move method")

class Teacher:
    def __init__(self,subject):
        self.subject = subject

    def teach(self):
        print("teach method")

class PartTimeTeacher(Person,Teacher):
    def __init__(self,name,subject,hours_per_week):
        self.name = name
        self.subject = subject
        self.hours_per_week = hours_per_week

teacher = PartTimeTeacher("a","math",2)

print(teacher.name)
print(teacher.subject)
print(teacher.hours_per_week)

teacher.move()
teacher.teach()