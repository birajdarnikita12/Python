# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

for i in range(6):
    m=int(input("Enter marks : "))
    marks.append(m)
marks.sort()
print(marks)