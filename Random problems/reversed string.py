"""string = input("Insert a word: ")
reversed_char = ''
for i in string:
    reversed_char = i + reversed_char
print(reversed_char)"""

#or 
name = 'Natty'
rever = ''
for i in range(len(name)-1, -1, -1):
    rever += name[i]
    
print(rever)