# Write a program to find whether a given username contains less than 10 characters or not.
username = input("Enter username: ")
if(len(username)<10):
    print("Length is less than 10:",len(username))
else:
    print("Length is greater than 10:", len(username))