# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks1 = int(input("Enter marks1: "))
marks2 = int(input("Enter marks2: "))
marks3 =int(input("Enter marks3: "))
percentage = (marks1+marks2+marks3)/3

if((marks1>=33)and(marks2>=33)and(marks3>=33)and percentage>=40):
    print("Pass:",percentage)
else:
    print("Fail:",percentage)
