class StudentDatabase:
    student_list = []
    @classmethod
    def add_student(cls,student):
        cls.student_list.append(student)

class Student:
    def __init__(self,student_id,name,department):
        self.__id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = False
        StudentDatabase.add_student(self)
    
    def enroll_student(self):
        if self.is_enrolled == False:
            self.is_enrolled = True
        
    def drop_student(self):
        self.is_enrolled = False
    
    def view_student_info(self):
        print(
            f'Student name:{self.name} '
            f'id:{self.__id} '
            f'Department:{self.department} '
            f'Enrollment status:{self.is_enrolled}'
        )
Rahim = Student('S1', 'Rahim Khan', 'CSE')
Karim = Student('S2', 'Karim Ahmed', 'EEE')
Sajim = Student('S3', 'Sajim Islam', 'BBA')
Ayesha = Student('S4', 'Ayesha Rahman', 'Pharmacy')
Tania = Student('S6', 'Tania Akter', 'Law')
Rakib = Student('S7', 'Rakib Hasan', 'Civil')
Mim = Student('S8', 'Mim Akter', 'Architecture')

while True:
    x = int(input(
    'Enter your choice:\n'
    '1. View All Students\n'
    '2. Enroll Student\n'
    '3. Drop Student\n'
    '4. Exit\n'
))
    
    match x:
        case 1:
            for student in StudentDatabase.student_list:
                student.view_student_info()
        case 2:
            name = input('Enter student name:')
            found = False
            for student in StudentDatabase.student_list:
                
                if student.name == name:
                    found = True
                    if student.is_enrolled == False:
                        student.enroll_student()
                        print(f'{name} is enrolled successfully.')
                    else:
                        print(f'{name} is already enrolled.')
            if found == False:
                print(f'{name} is not found in database.')
                
        case 3:
            name = input('Enter student name:')
            found = False
            for student in StudentDatabase.student_list:
               
                if student.name == name:
                    found = True
                    if student.is_enrolled == True:
                        student.drop_student()
                        print(f'{name} is dropped successfully.')
                    else:
                        print(f'{name} is not enrolled')
            if found == False:
                print(f'{name} is not found in database')
        case 4:
            print('Program terminated')
            break

        

