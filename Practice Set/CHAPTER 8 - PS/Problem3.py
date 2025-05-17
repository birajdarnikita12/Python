# Write a recursive function to calculate the sum of first n natural numbers.

'''
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3
sum(n)=1+2+3+...+n-1+n
sum(n)=sum(n-1)+n
'''
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

a = int(input("Enter a no: "))
print(f"sum of first n natural numbers: {sum(a)}")