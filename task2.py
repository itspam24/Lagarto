class Student:
    def __init__(self, name, age, course):
      self.name = name
      self.age = age
      self.course = course

    def introduce(self):
       print(f"Hi my name is {self.name}. I am {self.age} years old and I am studying {self.course}.")

student1 = Student("Hera", 19, "Culinary")
student2 = Student("Lexus", 23, "Hospitality Management")
student3 = Student("Percy", 20, "Information Technology")

student1.introduce()
student2.introduce()
student3.introduce()