# Create a student class that takes name & marks of 3 subject as arguments in constructure. Then create a method to print the average.

class Student:
    def __init__(self, name, marks): #marks is a list
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum+=i
        print("Hi", self.name, "Your average score is:", sum/3)
    
s1 = Student("Nikita,", [91, 99, 98])
s1.get_avg()
