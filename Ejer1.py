class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def studying(self):
        print(f"{self.name} is studying")


name1 = input("Add name: ")
age1 = input("Add age: ")
grade1 = input("Add grade: ")
student1 = Student(name1, age1, grade1)
student1.studying()
