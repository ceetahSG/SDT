class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}

    def add_classroom(self,classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self,subject,teacher):
        self.teachers[subject] = teacher

    def student_admission(self,student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if marks>=80 and marks <=100:
            return 'A+'
        elif marks>=70 and marks <80:
            return 'A'
        elif marks>=60 and marks <70:
            return 'A-'
        elif marks>=55 and marks <60:
            return 'B'
        elif marks>=50 and marks <55:
            return 'C'
        elif marks>=45 and marks <50:
            return 'D'
        elif marks>=33 and marks <45:
            return 'C'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_map ={
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.50,
            'D' : 2.00,
            'E' : 1.50,
            'F' : 1.00,
        }
        return grade_map.get(grade, 0.0)

    @staticmethod
    def value_to_grade(value):
        if value == 5:
            return 'A+'
        elif value >=4 and value <5:
            return 'A'
        elif value >=3.50 and value <4:
            return 'A-'
        elif value >=3 and value <3.50:
            return 'B'
        elif value >=2.50 and value <3:
            return 'C'
        elif value >=2 and value <2.50:
            return 'D'
        elif value >=1.50 and value <2:
            return 'E'
        else:
            return 'F'
    def __repr__(self):
        for key in self.classrooms.keys():
            print(key)
        print("ALL Students")

        result = ''
        for key,value in self.classrooms.items():
            result += f"---------{key.upper()} Classroom Students-------------\n"
            for student in value.students:
                result += f"{student.name}\n"
        print(result)

        subject = ''
        for key,value in self.classrooms.items():
            subject += f"---------{key.upper()} Classroom Subjects-------------\n"
            for sub in value.subjects:
                subject += f"{sub.name}\n"
        print(subject)

        teacher = ''
        for key in self.teachers.keys():
            teacher += f'{key}\n'
        print(teacher)

        print("Student's Result\n")
        for key,value in self.classrooms.items():
            for student in value.students:
                for k,i in student.marks.items():
                    print(student.name,k,i,student.subject_grade.get(k))
                if student.subject_grade:
                    print(student.name,student.final_grade())
        return ''



        
            
            