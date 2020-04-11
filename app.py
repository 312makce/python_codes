class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf', [45, 56, 67, 88])
student_two = Student('Nekus', [56, 87, 99, 54])
print(student_one.grades)