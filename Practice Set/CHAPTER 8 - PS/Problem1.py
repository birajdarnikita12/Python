# Write a program using functions to find greatest of three numbers

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    elif(c>a and c>b):
        return c
    
a = int(input("Enter a no 1: "))
b = int(input("Enter a no 2: "))
c = int(input("Enter a no 3: "))
print(f"The greatest no is: {greatest(a,b,c)}")