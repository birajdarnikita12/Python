# Print name and marks of Student

class Student:
    college_name = "ABC College"
    # Default constructor
    def __init_(self):
        pass

    # Parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Nikita",100)
s2 = Student("Nil",90)

print(s1.name, s1.marks, Student.college_name)
print(s2.name, s2.marks, s2.college_name)

        