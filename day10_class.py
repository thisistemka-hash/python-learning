class Student:
        def __init__(self, name):
            self.name = name
            self.grade = []
        def add_grade(self, grade):
            self.grade.append(grade)
        def average(self):
            if len(self.grade) == 0:
                return 0
            return sum(self.grade) / len(self.grade)   
        def show(self):
            print(f"{self.name}: {self.grade}, средний бал {self.average()}")

s1 = Student("Артём")
s1.add_grade(10)
s1.add_grade(9)
s1.add_grade(6)
s1.add_grade(3)
s1.add_grade(8)
s1.add_grade(1)
s1.show()