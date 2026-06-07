from school import School
from person import Student,Teacher
from subject import Subject
from classroom import Classroom

school = School("Bepza","Dhaka")

eight = Classroom("Eight")
nine = Classroom("Nine")
ten= Classroom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

rahim = Student("Rahim",eight)
karim = Student("Karim",nine)
hamim = Student("Hamim",ten)
fahim = Student("Fahim",ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(hamim)
school.student_admission(fahim)

abul = Teacher("Abul khan")
babul = Teacher("Babul khan")
kabul = Teacher("Kabul khan")

bangla = Subject("Bangla",abul)
english = Subject("English",babul)
physics = Subject("Physics",kabul)
chemistry = Subject("chemistry",kabul)

eight.add_subject(bangla)
eight.add_subject(english)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(chemistry)
ten.add_subject(english)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()
print(school)

