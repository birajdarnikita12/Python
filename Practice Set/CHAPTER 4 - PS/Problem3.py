# Check that a tuple type cannot be changed in python.

a = (33,55,"Nikita")
a[2]="N" #output - TypeError: 'tuple' object does not support item assignment
