# Write a program to fill in a letter template given below with name and date.
"""'letter = '''
Dear <|Name|>,
You are selected!
<|Date|>"""

letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''
name = input("Enter name:")
date = input("Enter date:")

print(letter.replace("<|Name|>",name).replace("<|Date|>",date))