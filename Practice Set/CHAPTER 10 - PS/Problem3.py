# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a=4

d1=Demo()
print(d1.a)

d1.a = 0
print(d1.a)

print(Demo.a)
# No