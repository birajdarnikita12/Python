# Write a python program using function to convert Celsius to Fahrenheit.

def f_to_c(f):
    c=(5/9)*(f-32)
    return c

t = int(input("Enter temperature: "))
print(f"{t} Fahrenheit = {f_to_c(t)} degree celsius ")