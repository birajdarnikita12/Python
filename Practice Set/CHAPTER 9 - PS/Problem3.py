# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

def generateTable(n):
    table = ""
    for i in range(1,11):
        # print(f"{n} X {i} = {n*i}")
        table += f"{n} X {i} = {n*i}\n"
    with open(f"N:/Tech/Python/Practice Set/CHAPTER 9 - PS/Table/table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)