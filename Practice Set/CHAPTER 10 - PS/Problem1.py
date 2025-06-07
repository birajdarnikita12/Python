# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p1 =Programmer("Nikita", 1200000,413516)
p2 =Programmer("Nil", 2000000,413512)
print(p1.name, p1.salary,p1.pin, p1.company)
print(p2.name, p2.salary,p2.pin, p2.company)