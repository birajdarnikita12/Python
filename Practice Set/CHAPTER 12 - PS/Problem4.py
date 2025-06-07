# Add a static method in problem 2, to greet the user with hello.

#(problem-2 ) Write a class “Calculator” capable of finding square, cube and square root of a number
import math
class Calculator:
    @staticmethod
    def greet():
        print("Hello there")

    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube (self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The square root is {math.sqrt(self.n)}")
    

a = Calculator(9)
a.greet()
a.square()
a.cube()
a.squareRoot()
