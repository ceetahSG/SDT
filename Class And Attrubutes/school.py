class Student:
    def __init__(self,name,age,current_class):
        self.name = name
        self.age = age
        self.current_class = current_class
    
    def __repr__(self) ->str:
        return f'Student name is {self.name}, class:{self.current_class}, age:{self.age}'
class Teacher:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
    def __repr__(self)->str:
        return f'Teacher name is {self.name}, Subject:{self.subject}'
class School:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_teacher(self,name,subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name,subject)
        self.teachers.append(teacher)

    def enroll_students(self,name,age,current_class,fee):
        if fee<6500:
            print ('No enough fee')
        else:
            id = len(self.students) + 1
            student = Student(name,age,current_class)
            self.students.append(student)
            print (f'{name} is enrolled with id:{id}, extra money {fee - 6500}')
    def __repr__(self)->str:
        print('Welcome to', self.name)
        print('-----------Our Faculty Members----------------')
        for teacher in self.teachers:
            print(teacher)
        print('-----------Our Students ----------------')
        for student in self.students:
            print(student)
        return 'All done for now'



ulab = School('ULAB')
ulab.enroll_students('Sajim',25,12,8500)
ulab.enroll_students('Rahim',22,12,7500)

ulab.add_teacher('Tom cruise','Algorithm')
ulab.add_teacher('Tom Holand','DSA')

print(ulab)

     