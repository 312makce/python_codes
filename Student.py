class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.mark = []

    def average(self):
        return sum(self.mark) / len(self.mark)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super(WorkingStudent, self).__init__(name, school)
        self.salary = salary
    @property
    def weekly_salary(self):
        return self.salary * 40

melis = WorkingStudent('Melis', 'IAAU', 55)
print(melis.salary)
melis.mark.append(77)
melis.mark.append(87)
print(f'average of your marks {melis.average()} ')
print(melis.weekly_salary)


# test short cuts for git commit