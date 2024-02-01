####################################################

class Student:
    school_name = 'ABC School'
    skills = []
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        
    def teach_skills(self, skill_name):
        self.skills.append(skill_name)
        
####################################################
        
s1 = Student('Siri', 10)
print(s1.name, s1.roll_no, Student.school_name)

s2 = Student('Rakshi', 77)
print(s2.name, s2.roll_no, Student.school_name)

#It is a good habit to:
#access class variable with class name (Student.school_name).

#accessing and modifying class variable with
#object name create a new instance variable,
#which shadows the class variable.
####################################################

s1.teach_skills('chess')
s1.teach_skills('rubics')

print(f'\nsiri skills {s1.skills}\n')

print(f'\nrakhi skills {s2.skills}\n')

####################################################

