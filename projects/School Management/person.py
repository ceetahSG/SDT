import random
from school import School
class Person:
    def __init__(self,name):
        self.name = name
    
class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def evaluate_exam(self):
        return random.randint(70,100)

class Student(Person):
    def __init__(self, name,classroom):
        super().__init__(name)
        self.classroom = classroom
        self.marks = {}
        self.subject_grade = {}
        self.grade = None
        self.__id = None
    
    def final_grade(self):
        total = 0
        grades = list(self.subject_grade.values())
        if not grades:
            return 'N/A'
        for grade in grades:
            point = School.grade_to_value(grade)
            total += point
        gpa = total / len(grades)
        return School.value_to_grade(gpa)
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value
