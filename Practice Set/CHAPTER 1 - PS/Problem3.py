# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.

import os

# Specify the directory path
directory_path = '/Tech/Python'

# List all entries in the directory
entries = os.listdir(directory_path)
   
for e in entries:
    print(e)
