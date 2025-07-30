import csv 

class Student:
    def __init__ (self, name):
        self.name = name
        self.grades = {}
    
    def add_grade (self, subject, grade):
        self.grades[subject] = grade

    def average_grade (self):
        counter = 0
        total = 0

        if not self.grades:
            return "N/A"
        
        for key, vals in self.grades.items():
            total += vals
            counter += 1
        
        average = int(total/counter)
        
        return average 
    
    def __str__(self):
        return f"{self.name} has average grade of {self.average_grade()}"

class Classroom:
    def __init__ (self, name):
        self.name = name
        self.students = {}
    
    def add_student (self, name):
            if name not in self.students:
                self.students[name] = Student(name)
            return self.students[name]
    
    def add_grade (self, student_name, subject, grade):
        self.students[student_name].add_grade(subject, grade)

    def writing_to_file (self):
        with open ('studentgrades.csv', 'w') as file:
            file.write('name subject grade\n')
            for student in self.students.values():
                for subject, grade in student.grades.items():
                    file.write(f"{student.name} {subject} {grade}\n")

    def load_from_csv(self):
        with open('studentgrades.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  

            for name, subject, grade in reader:
                if name not in self.students:
                    self.students[name] = Student(name)
                self.students[name].add_grade(subject, int(grade))


classroom = Classroom("Year 10")
tommy = classroom.add_student("Tommy")
classroom.add_student("Alice")
tommy.add_grade("Math", 85)
classroom.add_grade ("Alice", "Science", 94)
classroom.writing_to_file()  


