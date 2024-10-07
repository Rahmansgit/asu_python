import math

class Student:
    def __init__(self, first_name, last_name, gender, year, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.year = year
        self.gpa = gpa

    def show_student(self):
        print(f"Name: {self.first_name} {self.last_name}, Gender: {self.gender}, Year: {self.year}, GPA: {self.gpa:.2f}")

    def student_study_time(self, study_time):
        # Increasing GPA using the provided formula
        increase = math.log(study_time)
        self.gpa += increase
        
        # Ensuring GPA does not exceed 4.0
        if self.gpa > 4.0:
            self.gpa = 4.0

# Creating student objects
student_GPA = [
    Student("Alice", "Smith", "Female", "First-Year", 3.5),
    Student("Bob", "Johnson", "Male", "Sophomore", 3.2),
    Student("Charlie", "Williams", "Male", "Junior", 3.8),
    Student("Diana", "Jones", "Female", "Senior", 3.0),
    Student("Eva", "Brown", "Female", "Senior", 2.9)
]

# Displaying initial student information
print("Initial student information:")
for student in student_GPA:
    student.show_student()

# Study times in minutes
study_times = [30, 60, 90, 120, 180]

# Updating GPAs based on study time
for student, study_time in zip(student_GPA, study_times):
    student.student_study_time(study_time)

# Displaying updated student information
print("\nUpdated student information after studying:")
for student in student_GPA:
    student.show_student()