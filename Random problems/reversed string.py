string = str(input("Insert a word: "))
reversed_char = ''
for i in string:
    reversed_char = i + reversed_char
print(reversed_char)