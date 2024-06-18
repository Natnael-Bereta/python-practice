# print("Insert a number to check weather it is palindrome or not.")
# Input = int(input(">  "))
Input = int(input("Insert a number to check whether it is a palindrome or not. \n >"))
numbers = str(Input)
inverted = ''
for number in numbers:
    inverted = number + inverted

if inverted == numbers:
    print("It's a palindrom!")
else:
    print("It's not a palindrome!")