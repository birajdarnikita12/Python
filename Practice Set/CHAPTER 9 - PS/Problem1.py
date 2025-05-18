# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

f=open("N:/Tech/Python/Practice Set/CHAPTER 9 - PS/poems.txt")
data = f.read()
print(data)
if("twinkle" in data):
    print("Twinkle is present in the file")
else:
    print("Twinkle is not present in the file")

f.close()